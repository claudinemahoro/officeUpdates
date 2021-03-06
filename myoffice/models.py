from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from datetime import datetime
# from pyuploadcare.dj.models import ImageField

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=30)
    department_unit = models.CharField(max_length=30)
    director_pic = models.ImageField(upload_to='images/')
    # profile_picture = models.ImageField(upload_to='images/')
    employees_count = models.IntegerField(null=True)
    office_contact = PhoneNumberField(blank=False)
    director_contact = PhoneNumberField(blank=False)

    @classmethod
    def get_all_departments(cls):
        departments = cls.objects.all()
        return departments

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    department = models.ManyToManyField(Department)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='static/images/',blank=False)
    bio = HTMLField()

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = HTMLField(max_length=70)
    post_user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    post_department = models.ForeignKey(Department, related_name="posts", on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_all_posts(cls):
        posts = cls.objects.all()
        return posts