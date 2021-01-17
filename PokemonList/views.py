from django.shortcuts import render
from django.views import generic

# Create your views here.

class index(generic.TemplateView):
    template_name = 'PokemonList/index.html'
