from django.contrib import admin
from .models import GameState

@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    list_display = [
        'team_red_name', 'team_red_score', 
        'team_blue_name', 'team_blue_score',
        'round_number', 'game_time', 'penalty_time',
        'game_running', 'penalty_running'
    ]
    list_editable = [
        'team_red_score', 'team_blue_score',
        'round_number', 'game_time', 'penalty_time',
        'game_running', 'penalty_running'
    ]