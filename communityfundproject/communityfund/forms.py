from django import forms
from django.contrib.auth.models import User
from communityfund.models import Communities, Interests, CommunityProjects, UserProfile

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
