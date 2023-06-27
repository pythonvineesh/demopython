from . import views
from django.urls import path

urlpatterns = [

    path('',views.zero,name='zero'),
 #   path('add/',views.addition,name='addition')
]
