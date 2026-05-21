from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Prefetch
from album.models import Team, Player

class TeamListView(ListView):
    model = Team
    paginate_by = 12

class TeamDetailView(DetailView):
    model = Team
    queryset = Team.objects.prefetch_related(
        Prefetch('get_players', queryset=Player.objects.all())
    )
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = self.object.get_players.all()
        return context
