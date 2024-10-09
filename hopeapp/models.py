from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserType(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type=models.CharField(max_length=10,null=True)
class Registration(models.Model):
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=50,blank=False)
    password=models.CharField(max_length=50,null=True)
class TherapistRegistration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
       
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=True)
    name=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=50,null=True)
    regnum=models.CharField(max_length=50,null=True,unique=True)
    therapy_type=models.CharField(max_length=50,null=True)
    about=models.CharField(max_length=5000,null=True)
    hname=models.CharField(max_length=50,null=True)
    fees=models.CharField(max_length=20,null=True)
    image=models.ImageField(null=True)
    wtime=models.CharField(max_length=50,null=True)
    exp=models.CharField(max_length=123,null=True)
    quali=models.CharField(max_length=100,null=True)
    pincode=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=50,null=True)
class Add_Category(models.Model):
    category_name = models.CharField(max_length=50)
class PostDepressionSolutions(models.Model):
    therapy=models.ForeignKey(TherapistRegistration,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(Add_Category,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50,null=True)
    solutions=models.CharField(max_length=2500,null=True)
    image=models.ImageField(null=True)

class BookedTherapists(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    therapy=models.ForeignKey(TherapistRegistration,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=10,null=True)
    payment_date = models.DateField(null=True, blank=True)
    expiry_date=models.CharField(max_length=20,null=True,blank=True)

class Problems(models.Model):
    bk=models.ForeignKey(BookedTherapists,on_delete=models.CASCADE,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    message = models.TextField(null=True)
    status=models.CharField(max_length=50,null=True)
class Rating(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,null=True)
    therapist=models.ForeignKey(TherapistRegistration,on_delete=models.CASCADE,null=True)
    star=models.CharField(max_length=22, null=True)
    comment=models.CharField(max_length=22, null=True)
    status = models.CharField(max_length=22, null=True)
    # provider=models.ForeignKey(ServicerRegistration,on_delete=models.CASCADE,null=True)
