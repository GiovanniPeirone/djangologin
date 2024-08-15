from django.urls import path
from . import views

urlpatterns = [
    path('portal/', views.register, name='Portal'),
    path('xd/', views.xd, name='xd'),
]