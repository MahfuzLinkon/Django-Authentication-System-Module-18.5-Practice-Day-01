from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('change-password/', views.change_password, name='change-password'),
    path('change-password2/', views.change_password2, name='change-password2'),
]
