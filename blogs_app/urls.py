from django.urls import  path
from . import views

urlpatterns = [
    #this is for the root
    path("",views.home,name='home'),
]
