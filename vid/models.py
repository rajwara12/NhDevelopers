from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(  max_length=30)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self)   :
        return self.user.username
 



class Contact(models.Model):
    name = models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()

    def __str__(self)  :
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    img = models.ImageField(upload_to="images")
    views = models.IntegerField(default=0)
    def __str__(self) : 
        return self.title + '  by  ' + self.author.username



class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True )
    comment = models.TextField(max_length=300)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)  
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True) 
    timestamp = models.DateTimeField(default=now)  

    def __str__(self) :
        return self.comment[0:13]+ "... " + " by " +  self.user.username