from django.urls import path
from . import views

app_name = 'password_generator'

urlpatterns = [
    path('', views.generator, name='generator'),
    path('password', views.password, name='password')
]