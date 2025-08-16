from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, PermissionsMixin
import shortuuid

# class User(AbstractUser, PermissionsMixin):
#   avatar = models.ImageField(upload_to='avatars/', default="images/avatars/mist.png")
#   username = models.CharField(max_length=20)
#   email = models.EmailField(unique=True)

#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = []

class ProductType(models.Model):
  type = models.CharField(max_length=20)

  def __str__(self):
    return self.type

class Products(models.Model):
  producttype = models.ForeignKey(ProductType, related_name='typeofproduct', on_delete=models.SET_NULL, null =True)
  name = models.CharField(max_length=20)
  id = models.CharField(primary_key=True, default=shortuuid.uuid, unique=True, max_length=30)
  image = models.ImageField(upload_to='products/')
  price = models.IntegerField()
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created']

  def __str__(self):
    return self.name