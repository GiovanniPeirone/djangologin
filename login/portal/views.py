from django.http import HttpResponse
from django.template import loader

def xd(request):
    return HttpResponse("hello world")


def register(request):
  direccion = "template/index.html"
  template = loader.get_template(direccion)
  return HttpResponse(template.render())
# Create your views here.