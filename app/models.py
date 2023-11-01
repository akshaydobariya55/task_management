from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_developer = models.BooleanField('is_developer',default=False)
    is_manager = models.BooleanField('is_manager',default=False)
    is_admin = models.BooleanField('is_admin',default=False)


class Project(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    list_of_team_member = models.ForeignKey(User,on_delete=models.CASCADE)


Priority_choice = (
    ('Low','Low'),
    ('Medium','medium'),
    ('High','High'),
)
status_choice = (
    ('To do','To do'),
    ('Progress','Progress'),
    ('Done','Done')
)

class Task(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    priority = models.CharField(max_length=50,choices=Priority_choice)
    status = models.CharField(max_length=50,choices=status_choice)
    select_developer =models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    # title = models.ForeignKey(Task,on_delete=models.CASCADE)
    title =models.ForeignKey(Task,on_delete=models.CASCADE)
    issue = models.CharField(max_length=255)