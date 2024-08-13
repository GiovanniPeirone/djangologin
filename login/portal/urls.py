from django.urls import path
from . import views

urlpatterns = [
    path('portal/', views.register, name='register'),
    path('xd/', views.xd, name='xd'),
]