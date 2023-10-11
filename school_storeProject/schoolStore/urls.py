from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
urlpatterns = [

    path("",views.index,name="index" ),
    path("details",views.details,name="details" ),
    path("confirmed",views.confirmed,name="confirmed" ),

]