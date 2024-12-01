from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True, default='images/default_profile.png')
    birthdate = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)

    school = models.CharField(max_length=150, blank=True, null=True)
    college = models.CharField(max_length=150, blank=True, null=True)
    university = models.CharField(max_length=150, blank=True, null=True)
    mobile_number = PhoneNumberField(blank=True, null=True)  

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)  

    def __str__(self):
        return f"{self.user.username}'s Profile"
