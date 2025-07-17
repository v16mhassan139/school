from django.urls import path
from .views import  *

urlpatterns=[
    path('', home_page,name='home'),
    path('about/',about_page,name='about'),
    path ('sign_in/',Sign_in,name='signin')
  
]
