# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy 
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from .models import Persona


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))


class Registrar(CreateView):
    template_name = "registrar.html"
    model = Persona
    success_url = reverse_lazy('registrado')


class Registrado(TemplateView):
    template_name = "registrado.html"


class Consultar(ListView):
    model = Persona
    template_name = "consultar.html"
    context_object_name = "lista"
