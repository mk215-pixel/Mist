from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),

    path('add/', addProduct, name='add-product'),
    path('edit/<str:pk>/', editProduct, name="edit-product"),
    path('delete/<str:pk>/', delete, name='delete' ),

    path('add_user/', addUser, name='add-user'),
    path('edit_user/<str:pk>/', editUser, name='edit-user' ),
    path('login user/', loginUser, name="login"),
    path('logout user/', logoutUser, name="logout"),

    path('filters/', filters, name='filters')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
