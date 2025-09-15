from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=40)
    text=models.TextField()
    posted_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    commented_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} : {self.comment}"
    
