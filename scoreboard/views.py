from django.shortcuts import render, redirect
from .models import GameState

def get_state():
    state, created = GameState.objects.get_or_create(id=1)
    return state

# models.py
from django.db import models



def viewer(request):
    state = get_state()
    return render(request, "viewer.html", {"state": state})

def admin_dashboard(request):
    state = get_state()
    return render(request, "admin_dashboard.html", {"state": state})

def increment_score(request, team):
    state = get_state()
    if team == "red":
        state.team_red_score += 1
    elif team == "blue":
        state.team_blue_score += 1
    state.save()
    return redirect("admin_dashboard")

def decrement_score(request, team):
    state = get_state()
    if team == "red" and state.team_red_score > 0:
        state.team_red_score -= 1
    elif team == "blue" and state.team_blue_score > 0:
        state.team_blue_score -= 1
    state.save()
    return redirect("admin_dashboard")

def next_round(request):
    state = get_state()
    state.round_number += 1
    state.save()
    return redirect("admin_dashboard")

def reset_timer(request):
    state = get_state()
    state.game_time = 180
    state.game_running = False
    state.save()
    return redirect("admin_dashboard")

def toggle_timer(request):
    state = get_state()
    state.game_running = not state.game_running
    state.save()
    return redirect("admin_dashboard")

def reset_penalty(request):
    state = get_state()
    state.penalty_time = 10
    state.penalty_running = True
    state.save()
    return redirect("admin_dashboard")
