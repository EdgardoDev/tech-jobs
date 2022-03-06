from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('current-user/', views.currentUser, name='current_user'),
]
