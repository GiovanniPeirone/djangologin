from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

def xd(request):
    return HttpResponse("hello world")


def register(request):
  return render(request, 'portal/template/index.html')
# Create your views here.