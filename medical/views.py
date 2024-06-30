from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Medical
from .forms import MedicalForm

class List(generic.ListView):
    model = Medical
    
class Create(generic.CreateView):
    model = Medical
    form_class = MedicalForm
    success_url = reverse_lazy('medical:list')

# Create your views here.
