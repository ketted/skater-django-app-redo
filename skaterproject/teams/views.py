from typing import List
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import TeamForm
from .models import Team
# Create your views here.

class TeamList(ListView):
    model = Team
    template_name = 'team-index.html.django'
    context_object_name = 'teams'
    # ****** OR DID I WRITE PLURAL?

class TeamDetail(DeleteView):
    model = Team
    template_name = 'team-detail.html.django'
    context_object_name = 'team'

class TeamCreate(CreateView):
    model = Team
    template_name = 'add-team.html.django'
    fields = TeamForm.Meta.fields
    success_url = reverse_lazy('teams-home')

class TeamUpdate(UpdateView):
    model = Team
    template_name = 'edit-team.html.django'
    fields = TeamForm.Meta.fields
    success_url = reverse_lazy('teams-home')

class TeamDelete(DeleteView):
    model = Team
    template_name = 'delete-team.html.django'
    success_url = reverse_lazy('teams-home')