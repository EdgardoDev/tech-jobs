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
    
    
class Field(models.TextChoices):
    SOFTWARE_DEVELOPMENT = 'Software Development'
    NETWORK_ENGINEERING = 'Network Engineering'
    USER_SUPPORT = 'User Support'
    PROJECT_MANAGEMENT = 'Project Management'
    WEB_DEVELOPMENT = 'Web Development' 
    INFORMATION_SECURITY = 'Information Security'
    SYSTEM_ARCHITECTURE = 'Systems Architecture'
    DATABASE_ADMINISTRATION = 'Database Administration'
    SYSTEMS_ADMINISTRATION = 'Systems Administration'
    
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
    experience = models.CharField(
        max_length=20,
        choices=Experience.choices,
        default=Experience.ENTRY_LEVEL
    )
    field = models.CharField(       
        max_length=30,
        choices=Field.choices,
        default=Field.SOFTWARE_DEVELOPMENT
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
        
        print(g)
        
        lng = g.lng
        lat = g.lat
        
        self.point = Point(lng, lat)
        super(Job, self).save(*args, **kwargs)
        
        
        
class CandidatesApplied(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    resume = models.CharField(max_length=200)
    appliedAt = models.DateTimeField(auto_now_add=True)