from django.db import models
from django.contrib.auth.models import User
import geocoder
import os
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point
from datetime import *
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class JobType(models.TextChoices):
    FULL_TIME = 'Full-Time'
    CONTRACT = 'Contract'
    PART_TIME = 'Part-Time'
    TEMPORARY = 'Temporary'
    INTERNSHIP = 'Internship'
 
  
class Education(models.TextChoices):
    BACHELORS = 'Bachelors'
    MASTERS = 'Masters'
    PHD = 'Phd'
    
    
class Experience(models.TextChoices):
    ENTRY_LEVEL = 'Entry Level'
    MID_LEVEL = 'Mid Level'
    SENIOR_LEVEL = 'Senior Level'
    
    
class Skills(models.TextChoices):
    PYTHON = 'Python'
    SQL = 'SQL'
    JAVA = 'JAVA'
    C_PLUSPLUS = 'C++'
    JAVASCRIPT = 'JavaScript' 
    GO = 'Go'
    C_SHARP = 'C#'
    NODEJS = 'NodeJS'
    REACT = 'React'
    TYPESCRIPT = 'TypeScript'
    
def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)
    
    
class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models. CharField(max_length=100, null=True)
    jobType = models.CharField(
        max_length=10,
        choices=JobType.choices,
        default=JobType.FULL_TIME
    )
    education = models.CharField(
        max_length=10,
        choices=Education.choices,
        default=Education.BACHELORS
    )
    experience = models.CharField(
        max_length=10,
        choices=Experience.choices,
        default=Experience.ENTRY_LEVEL
    )
    skills = models.CharField(       
        max_length=10,
        choices=Skills.choices,
        default=Skills.PYTHON
    )
    education = models.CharField(
        max_length=10,
        choices=Education.choices,
        default=Education.BACHELORS
    )
    salary = models.IntegerField(
        default=1, 
        validators=[MinValueValidator(1), 
                    MaxValueValidator(1000000)
                    ]
        )
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0, 0.0))
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        g = geocoder.mapquest(self.address, key=os.environ.get('GEOCODER_API'))
        long = g.long
        lat = g.lat
        
        self.point = Point(long, lat)
        super(Job, self).save(*args, **kwargs)