from django.db import models

# Create your models here.

class PropertyInfo(models.Model):
    street_address = models.CharField(max_length=400)
    city_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pic')
    property_brochure = models.FileField(upload_to='brochure')
    status = models.CharField(max_length=10)

class ContactUs(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=500)
    post = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='news_pics')
