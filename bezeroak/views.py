from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from platerak.models import Platerak
from .models import Bezeroak

def bezeroak(request):
  bezeroak = Bezeroak.objects.all().values()
  platerak = Platerak.objects.all().values()
  template = loader.get_template('bezeroak.html')
  context = {'bezeroak' : bezeroak,
             'platerak' : platerak,
             }
  return HttpResponse(template.render(context, request))

def delete(request, id):
  platera = Bezeroak.objects.get(id=id)
  platera.delete()
  return HttpResponseRedirect(reverse('bezeroak'))
