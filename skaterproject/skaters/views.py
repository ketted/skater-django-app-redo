from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SkaterForm
from .models import Skater

# Create your views here.

class SkaterList(ListView):
    model = Skater
    template_name = 'index.html.django'
    context_object_name = 'skaters'

class SkaterDetail(DetailView):
    model = Skater
    template_name = 'detail.html.django'
    context_object_name = 'skater'

class SkaterCreate(CreateView):
    model = Skater
    template_name = 'add.html.django'
    fields = SkaterForm.Meta.fields
    success_url = reverse_lazy('home')

class SkaterDelete(DeleteView):
    model = Skater
    template_name = 'delete.html.django'
    success_url = reverse_lazy('home')

class SkaterUpdate(UpdateView):
    model = Skater
    template_name = 'edit.html.django'
    success_url = reverse_lazy('home')