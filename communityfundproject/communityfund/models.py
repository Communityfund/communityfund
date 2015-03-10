from django.db import models

class Communities(models.Model):
    community = models.CharField(max_length=32)
    province = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.community + ", " + self.province
        
class Users(models.Model):
    userName = models.CharField(max_length=32, unique=True)
    emailAddress = models.EmailField()
    password = models.CharField(max_length=32)
    community = models.ForeignKey(Communities, limit_choices_to={'community'})
    
    def __unicode__(self):
        return self.userName

class Interests(models.Model):
    interest = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.interest
        
class Projects(models.Model):
    projectName = models.CharField(max_length=32, primary_key=True)
    community = models.ForeignKey(Communities, limit_choices_to={'community'})
    interest = models.ForeignKey(Interests)
    initiator = models.ForeignKey(Users, limit_choices_to={'userName'})
    goal = models.IntegerField()
    amountFunded = models.IntegerField()
    backers = models.IntegerField()
    
    def __unicode__(self):
        return self.projectName + " - " + self.community + ", " + self.province
        
#class Payments(models.Model):
#    backer = models.ForeignKey(Users, limit_choices_to={'userName'})
#    projectID = models.ForeignKey(Projects)
#    amount = models.IntegerField()
#    isDonation = models.BinaryField()
#    timestamp = models.DateField()
    
#    def __unicode__(self):
#        return self.backer + ", " + self.project

#class Comments(models.Model):
#    commenter = models.ForeignKey(Users, limit_choices_to={'userName'}, related_name='commenter')
#    recipient = models.ForeignKey(Users, limit_choices_to={'userName'}, related_name='recipient')  
#    text = models.CharField(max_length=256)
#    timestamp = models.DateField()
    
#    def __unicide__(self):
#        return self.commenter + " to " + self.recipient + ": " + self.text
        
# Create your models here.
