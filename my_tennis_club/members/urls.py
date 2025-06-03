from django.urls import path
from . import views
from .views import hello_world
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),  # Remove the 'members/' prefix here
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('orderbyfirst/', views.orderbyfirst, name='orderbyfirst'),  
    path('descendingby/',views.descendingby,name='descendingby'),
    path('', views.homepage, name='home'),
    path('api/hello/',hello_world,name='hello_world ')
   
]
