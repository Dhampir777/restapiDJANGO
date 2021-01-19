# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def super_user(self,email,name,password):
            """create and save a new superuser with a given details"""

            user=self.create_user(email,name,password)
            user.is_superuser = True
            user.is_staff = True
            user.save(using=self._db)

            return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
# Create your models here.
    email=models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)


    objects= UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELS=['name']

    def get_full_name(self):
        """retrieve full name of user"""

        return self.name

    def get_short_name(self):
        """retrieve short name of user"""

        return self.name

    def __str__(self):
        """return string representation"""
        return self.email
