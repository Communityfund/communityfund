from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

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
    projectsCreated = models.IntegerField()
    projectsFunded = models.IntegerField()
    reputation = models.IntegerField()
    aboutText = models.CharField(max_length=1000)
    skills = models.CharField(max_length=1000)
    interests = models.CharField(max_length=1000)
    
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
    duration = models.IntegerField()
    dateCreated = models.DateTimeField()
    blurb = models.CharField(max_length=140)
    slug = models.SlugField()
    why = models.CharField(max_length=3000)
    who = models.CharField(max_length=3000)
    how = models.CharField(max_length=3000)
    support = models.CharField(max_length=3000)
    more = models.CharField(max_length=3000)
    rewards = models.CharField(max_length=3000)
    picture = models.ImageField(upload_to='projects', blank=True)
    
    def __unicode__(self):
        return self.projectName

class Payment(models.Model):
    backer = models.ForeignKey(User)
    project = models.ForeignKey(CommunityProject)
    amount = models.IntegerField()
    isDonation = models.BinaryField()
    timestamp = models.DateField()
    
    def __unicode__(self):
        return self.backer + ", " + self.timestamp

class Comment(models.Model):
    commenter = models.ForeignKey(User, related_name='commenter')
    recipient = models.ForeignKey(User, related_name='recipient')  
    text = models.CharField(max_length=1000)
    timestamp = models.DateTimeField()
    
    def __unicode__(self):
        return self.commenter + " to " + self.recipient + " at " + self.timestamp

class ProjectComment(models.Model):
    commenter = models.ForeignKey(User)
    project = models.ForeignKey(CommunityProject)
    text = models.CharField(max_length=1000)
    timestamp = models.DateTimeField()
    
    def __unicode__(self):
        return self.commenter + " to " + self.project + " at " + self.timestamp

class UserInterest(models.Model):
    interest = models.ForeignKey(Interests)
    user = models.ForeignKey(User)
          
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
