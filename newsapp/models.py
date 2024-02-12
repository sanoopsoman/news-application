from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=40)
    ViewPassword=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.username
    
    
# class Category(models.Model):
#     name=models.CharField(max_length=20,null=True)
#     img=models.ImageField(upload_to="gallery")
    
#     def __str__(self):
#         return self.name
    
class Staff_reg(models.Model):
    staff=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=10,null=True)
    img=models.ImageField(upload_to="gallery")
    address=models.TextField()
    qualification=models.CharField(max_length=50,null=True)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Officer_reg(models.Model):
    officer=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=10,null=True)
    img=models.ImageField(upload_to="gallery")
    address=models.TextField()
    qualification=models.CharField(max_length=50,null=True)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name
    
class User_reg(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=25,null=True)
    email=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=10,null=True)
    img=models.ImageField(upload_to="gallery")
    address=models.TextField()
    qualification=models.CharField(max_length=50,null=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name
    
    
class Add_news(models.Model):
    name=models.CharField(max_length=50,null=True)
    category=models.CharField(max_length=25,null=True)
    description=models.TextField()
    img=models.ImageField(upload_to="gallery")
    date=models.DateTimeField(auto_now_add=True)
    time=models.TimeField(auto_now=True)
    district=models.CharField(max_length=25,null=True,default="All")
    status=models.CharField(max_length=30,default="pending")
    sid=models.ForeignKey(Staff_reg,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class Usercomment(models.Model):
    uid=models.ForeignKey(User_reg,on_delete=models.CASCADE)
    comment=models.TextField(null=True)
    
    
class UserActions(models.Model):
    uid=models.ForeignKey(User_reg, on_delete=models.CASCADE)
    comment=models.TextField(null=True)
    status=models.CharField(max_length=10,default="unread")
    
class Likenews(models.Model):
    uid=models.ForeignKey(User_reg,on_delete=models.CASCADE)
    nid=models.ForeignKey(Add_news,on_delete=models.CASCADE)
    
class Dislikenews(models.Model):
    uid=models.ForeignKey(User_reg,on_delete=models.CASCADE)
    nid=models.ForeignKey(Add_news,on_delete=models.CASCADE)
    
    
