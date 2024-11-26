from django.db import models
from django.contrib.auth.models import User as SysUser

class User(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	sys_user = models.ForeignKey(SysUser,on_delete=models.CASCADE)

# Create your models here.
