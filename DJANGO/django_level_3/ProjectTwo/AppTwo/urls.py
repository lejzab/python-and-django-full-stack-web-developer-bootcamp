from django.urls import path
from . import views

urlpatterns = [
    path('users/',views.users, name='users'),
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('help/',views.help, name='help'),
]
