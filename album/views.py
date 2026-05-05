from django.shortcuts import render
from django.views.generic import ListView
from album.models import Team

class TeamListView(ListView):
    model = Team
