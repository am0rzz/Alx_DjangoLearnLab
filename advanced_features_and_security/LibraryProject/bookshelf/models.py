from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group, Permission


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length =200)
    author = models.CharField(max_length= 100)
    publication_year = models.IntegerField()

    class Meta:
        permessions = [
            ('can_view', 'Views Books'),
            ('can_create','Add Books'),
            ('can_edit','Edit Books'),
            ('can_delete','Delete Books')
        ]

# Create a Custom User.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

User = get_user_model()

class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, photo, password=None, **extra_fields):
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')
        user = self.model(date_of_birth=date_of_birth, profile_photo=photo, **extra_fields)
        user.set_password(password)
        return user

    def create_superuser(self, date_of_birth, photo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(date_of_birth, photo, password, **extra_fields)
    
Editors, created = Group.objects.get_or_create(name='can_edit')
Viewers, created = Group.objects.get_or_create(name='can_view')
Admins, created = Group.objects.get_or_create(name='can_delete')