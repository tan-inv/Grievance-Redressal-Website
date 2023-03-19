#match urls

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/',views.about, name ='complaint-about'),
    path('form/',views.form, name ='complaint-form'),
    path('user_home/',views.userhm, name ='complaint-user home'),
    path('user/', views.user, name ='complaint-user'),
    path('admin/',views.admin, name ='complaint-admin'),
]