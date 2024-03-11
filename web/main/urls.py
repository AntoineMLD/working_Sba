from django.urls import path
from main import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('form/', views.formulaire, name='formulaire'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')   
    
]