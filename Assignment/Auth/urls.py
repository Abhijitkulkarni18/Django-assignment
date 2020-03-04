from django.conf.urls import url
from django.urls import path,re_path
from .views import SignUp,LogIn

urlpatterns = [

    path(r'signup/',SignUp.as_view(),name='SignUp'),
    path(r'login/',LogIn.as_view(),name='LogIn')

]