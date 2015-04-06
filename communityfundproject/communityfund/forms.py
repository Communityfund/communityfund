from django import forms
from django.contrib.auth.models import User
from communityfund.models import Communities, Interests, CommunityProject, UserProfile, Payment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    firstName = forms.CharField(max_length=32)
    lastName = forms.CharField(max_length=32)
    community = forms.ModelChoiceField(queryset=Communities.objects.all())
    
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'community')

class ProjectForm(forms.ModelForm):
    projectName = forms.CharField(max_length=32)
    goal = forms.FloatField()
    blurb = forms.CharField(max_length=140, widget=forms.Textarea)
    duration = forms.IntegerField()
    interest = forms.ModelChoiceField(queryset=Interests.objects.all())
    why = forms.CharField(max_length=3000, widget=forms.Textarea)
    who = forms.CharField(max_length=3000, widget=forms.Textarea)
    how = forms.CharField(max_length=3000, widget=forms.Textarea)
    support = forms.CharField(max_length=3000, widget=forms.Textarea)
    more = forms.CharField(max_length=3000, widget=forms.Textarea)
    rewards = forms.CharField(max_length=3000, widget=forms.Textarea)
    
    class Meta:
        model = CommunityProject
        fields = ('projectName', 'interest', 'goal', 'blurb', 'duration', 'why', 'who', 'how', 'support', 'more', 'rewards', 'picture')

class PaymentForm(forms.ModelForm):
    amount = forms.FloatField()
    
    class Meta:
        model = Payment
        fields = ('amount')