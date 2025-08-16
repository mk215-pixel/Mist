from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
import os
from .models import *
from .forms import *

def home(request):
  q = request.GET.get('q') if request.GET.get('q') != None else  ''
  products = Products.objects.filter(producttype__type__icontains=q)
  context = {'products': products}
  return render(request, 'home.html', context)

def addProduct(request):
  form = ProductForm()
  product_type = ProductType.objects.all()


  if request.method == 'POST':
    type_of_product = request.POST.get('producttype')
    type, created = ProductType.objects.get_or_create(type=type_of_product)

    Products.objects.create(
      image=request.FILES.get('image'),
      producttype=type,
      name=request.POST.get('name'),
      price=request.POST.get('price'),
    )
    # form = ProductForm(request.POST, request.FILES)
    # if form.is_valid():
    #   form.save()
    #return redirect('home')

  context = {'form': form, 'producttype': product_type}
  return render(request, 'products/products_form.html', context)

def editProduct(request, pk):
  product = Products.objects.get(id=pk)
  form = ProductForm(instance=product)
  product_type = ProductType.objects.all()


  if request.method == 'POST':
    type_of_product = request.POST.get('producttype')
    type, created = ProductType.objects.get_or_create(type=type_of_product)
    
    if request.FILES:
      product.image=request.FILES.get('image')

    product.producttype=type
    product.name=request.POST.get('name')
    product.price=request.POST.get('price')

    product.save()

    return redirect('home')

  context = {'form': form, 'producttype': product_type}
  return render(request, 'products/product_edit.html', context)

def delete(request, pk):

  object = Products.objects.get(id=pk)

  if request.method == 'POST':
    object.delete()      
    return redirect('home')
  
  context = {'object': object}
  return render(request, 'delete.html', context)

def addUser(request):
  form = UserForm()

  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    else: 
      messages.error(request, 'Error occured, please try again')

  context = {'form': form}
  return render(request, 'User/user_form.html', context)

def editUser(request, pk):
  page = 'edit'

  user = User.objects.get(id=pk)
  form = UserForm(instance=user)

  if request.method == 'POST':
    form = UserForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect('home')

  context = {'form': form, 'page': page}
  return render(request, 'User/edit_user.html', context)

def loginUser(request):
  page = 'login' 

  if request.method == 'POST': 
    username = request.POST.get('username')
    password = request.POST.get('password')

    try: 
      user = User.objects.get(username=username)

    except:
      messages.error(request, 'Please register account')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    
    else:
      messages.error(request, 'An error occured')
    

  context = {'page': page}
  return render(request, 'User/user_form.html', context)

def logoutUser(request):
  logout(request)
  return redirect('home')

def filters(request):
  types = ProductType.objects.all()
  context = {'types': types}
  return render(request, 'filters.html', context)
