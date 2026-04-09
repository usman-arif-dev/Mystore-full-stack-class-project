
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='homepage'),
    path('signup', SignupFnc, name='signupurl'),
    path('signin', signinfnc, name='signinurl'),
    path('logout', logoutfnc, name='logouturl'),
    path('products', products, name='products'),
    path('addproduct', addproduct, name='addproduct'),
]