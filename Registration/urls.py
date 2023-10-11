from django.urls import path
from . import views
from .views import login



urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
    path('login/', login.as_view(), name='login'),
    
]