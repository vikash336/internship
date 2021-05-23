from django.db import models

from django.contrib.auth.models import User
class adviser(models.Model):
    adname=models.CharField(max_length=100)
    ad_id=models.IntegerField()
    bookingtime=models.IntegerField()
    bookid=models.IntegerField()
class owner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.nickname
