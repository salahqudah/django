from django.urls import path
from . import views
from .views import hello_world,HelloWorldAPIView,ItemList, ItemDetail,book_fbv, BookCBV, BookMixinView,render_fbv_form,render_cbv_form,render_mixin_form
urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),  # Remove the 'members/' prefix here
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('orderbyfirst/', views.orderbyfirst, name='orderbyfirst'),  
    path('descendingby/',views.descendingby,name='descendingby'),
    path('', views.homepage, name='home'),
    path('api/hello/',hello_world,name='hello_world '),
    path('api/greet/', HelloWorldAPIView.as_view(), name='hello-api'),
    path('api/items/', ItemList.as_view(), name='item-list'),
    path('api/items/<int:pk>/', ItemDetail.as_view(), name='item-detail'),
    path('fbv/', book_fbv, name='fbv'),
    path('cbv/', BookCBV.as_view(), name='cbv'),
    path('mixin/', BookMixinView.as_view(), name='mixin'),
    path('fbv/form/', render_fbv_form),
    path('cbv/form/', render_cbv_form),
    path('mixin/form/', render_mixin_form),

  

]
