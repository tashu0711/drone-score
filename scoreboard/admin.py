from django.contrib import admin
from .models import GameState

@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    list_display = ("team_red_name", "team_blue_name", "round_number", "team_red_score", "team_blue_score")
