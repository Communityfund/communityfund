from django.db import models
from django.contrib.auth.models import User

class Communities(models.Model):
    community = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.community + ", " + self.province

class Interests(models.Model):
    interest = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.interest

class UserProfile(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    user = models.OneToOneField(User)
    community = models.ForeignKey(Communities)
    
    def __unicode__(self):
        return self.user.username

class CommunityProject(models.Model):
    projectName = models.CharField(max_length=32)
    community = models.ForeignKey(Communities)
    interest = models.ForeignKey(Interests)
    initiator = models.ForeignKey(User)
    goal = models.IntegerField()
    amountFunded = models.IntegerField()
    backers = models.IntegerField()
    description = models.CharField(max_length=1000)
    duration = models.IntegerField()
    
    def __unicode__(self):
        return self.projectName

class Payment(models.Model):
    backer = models.ForeignKey(Users)
    project = models.ForeignKey(Projects)
    amount = models.IntegerField()
    isDonation = models.BinaryField()
    timestamp = models.DateField()
    
    def __unicode__(self):
        return self.backer + ", " + self.timestamp

class Comment(models.Model):
    commenter = models.ForeignKey(UserProfile, related_name='commenter')
    recipient = models.ForeignKey(UserProfile, related_name='recipient')  
    text = models.CharField(max_length=1000)
    timestamp = models.DateField()
    
    def __unicode__(self):
        return self.commenter + " to " + self.recipient + " at " + self.timestamp

class ProjectComment(models.Model):
    commenter = models.ForeignKey(Users)
    project = models.ForeignKey(Projects)
    text = models.CharField(max_length=1000)
    timestamp = models.DateField()
    
    def __unicode__(self):
        return self.commenter + " to " + self.project + " at " + self.timestamp
        
# DEPRECATED - Need to delete     
class Usernames(models.Model):
    userName = models.CharField(max_length=32, unique=True, primary_key=True)
    emailAddress = models.EmailField()
    password = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.userName

# DEPRECATED - REMOVE     
class CommunityProjects(models.Model):
    projectName = models.CharField(max_length=32, primary_key=True)
    community = models.ForeignKey(Communities)
    interest = models.ForeignKey(Interests)
    initiator = models.ForeignKey(Usernames)
    goal = models.IntegerField()
    amountFunded = models.IntegerField()
    backers = models.IntegerField()
    
    def __unicode__(self):
        return self.projectName
        
# Create your models here.
