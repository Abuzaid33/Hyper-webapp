from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('registration/', include('Registration.urls')),
    path('', include('Dashboard.urls')),
]
  
