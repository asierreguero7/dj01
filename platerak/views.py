from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Platerak

def platerak(request):
  platerak = Platerak.objects.all().values()
  template = loader.get_template('platerak.html')
  context = {
    'platerak': platerak,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['izena']
  y = request.POST['prezioa']
  platera = Platerak(izena=x, prezioa=y)
  platera.save()
  return HttpResponseRedirect(reverse('platerak'))

def delete(request, id):
  platera = Platerak.objects.get(id=id)
  platera.delete()
  return HttpResponseRedirect(reverse('platerak'))

def update(request, id):
  platera = Platerak.objects.get(id=id)
  platerak = loader.get_template('update.html')
  context = {
    'platera': platera,
  }
  return HttpResponse(platerak.render(context, request))

def updaterecord(request, id):
  izena = request.POST['izena']
  prezioa = request.POST['prezioa']
  platera = Platerak.objects.get(id=id)
  platera.izena = izena
  platera.prezioa = prezioa
  platera.save()
  return HttpResponseRedirect(reverse('platerak'))