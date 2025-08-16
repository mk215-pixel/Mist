from django.forms import ModelForm
from .models import Products
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']

class ProductForm(ModelForm):
  class Meta:
    model = Products
    fields = ['image', 'producttype', 'name', 'price']
    #widgets = 