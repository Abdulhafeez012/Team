from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Experience = models.TextField(null=True)
    DateOfBirth = models.DateField()
    ProfilePic = models.ImageField(upload_to='profile_pics', blank=True)
    Gender = models.CharField(max_length=10, choices=[('F', 'Female'), ('M', 'Male')])

    def __str__(self):
        return self.user.username
