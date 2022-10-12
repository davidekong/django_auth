from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'), 
    path('logIn/', views.logIn, name='logIn'), 
    path('dashboard', views.dashboard, name='dashboard'), 
    path('forgot_password/', views.forgot_password, name='forgot_password'), 
    path('change_password/<pk>', views.change_password, name='change_password')
]
