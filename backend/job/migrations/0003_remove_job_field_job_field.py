# Generated by Django 4.0.3 on 2022-03-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_remove_job_skills_job_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='Field',
        ),
        migrations.AddField(
            model_name='job',
            name='field',
            field=models.CharField(choices=[('Software Development', 'Software Development'), ('Network Engineering', 'Network Engineering'), ('User Support', 'User Support'), ('Project Management', 'Project Management'), ('Web Development', 'Web Development'), ('Information Security', 'Information Security'), ('Systems Architecture', 'System Architecture'), ('Database Administration', 'Database Administration'), ('Systems Administration', 'Systems Administration')], default='Software Development', max_length=30),
        ),
    ]