from django.db import models

class Communities(models.Model):
    community = models.CharField(max_length=32, primary_key=True)
    province = models.CharField(max_length=32, primary_key=True)
    
    def __unicode__(self):
        return self.name + ", " + self.province
        
class Users(models.Model):
    userName = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    community = models.ForeignKey(Communities)
    
    def __unicode__(self):
        return self.userName

class Projects(models.Model):
    projectName = models.CharField(max_length=32, primary_key=True)
    community = models.ForeignKey(Communities, limit_choices_to={'community'}, primary_key=True)
    province = models.ForeignKey(Communities, limit_choices_to={'province'}, primary_key=True)
    initiator = models.ForeignKey(Users, limit_choices_to={'userName'})
    goal = models.IntegerField()
    amountFunded = models.IntegerField()
    backers = models.IntegerField()
    
    def __unicode__(self):
        return self.projectName + " - " + self.community + ", " + self.province

class Payments(models.Model):
    backer = models.ForeignKey(Users, limit_choices_to={'userName'})
    project = models.ForeignKey(Projects, limit_choices_to={'id'})
    amount = models.IntegerField()
    isDonation = models.BinaryField()
    timestamp = models.DateField()
    
    def __unicode__(self):
        return self.backer + ", " + self.project

class Comments(models.Model):
    commenter = models.ForeignKey(Users, limit_choices_to={'userName'}, related_name='commenter')
    recipient = models.ForeignKey(Users, limit_choices_to={'userName'}, related_name='recipient')  
    text = models.CharField(max_length=256)
    timestamp = models.DateField()
    
    def __unicide__(self):
        return self.commenter + " to " + self.recipient + ": " + self.text
        
# Create your models here.
