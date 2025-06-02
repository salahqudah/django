
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('', include('members.urls')),  # This already includes the 'members/' prefix
    path('admin/', admin.site.urls),
]