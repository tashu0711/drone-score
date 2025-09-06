from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GameState

def get_game_state():
    game_state, created = GameState.objects.get_or_create(id=1)
    return game_state

def viewer(request):
    state = get_game_state()
    return render(request, 'viewer.html', {'state': state})

def admin_dashboard(request):
    state = get_game_state()
    return render(request, 'admin_dashboard.html', {'state': state})

def increment_score(request, team):
    state = get_game_state()
    if team == 'red':
        state.team_red_score += 1
    elif team == 'blue':
        state.team_blue_score += 1
    state.save()
    return redirect('admin_dashboard')

def decrement_score(request, team):
    state = get_game_state()
    if team == 'red':
        state.team_red_score = max(0, state.team_red_score - 1)
    elif team == 'blue':
        state.team_blue_score = max(0, state.team_blue_score - 1)
    state.save()
    return redirect('admin_dashboard')

def next_round(request):
    state = get_game_state()
    state.round_number += 1
    state.save()
    return redirect('admin_dashboard')

# views.py mein reset_timer function
def reset_timer(request):
    state = get_game_state()
    state.game_time = 180  # 3 minutes
    state.game_running = False
    state.save()
    return redirect('admin_dashboard')

# toggle_timer function
def toggle_timer(request):
    state = get_game_state()
    state.game_running = not state.game_running
    state.save()
    return redirect('admin_dashboard')

def reset_penalty(request):
    state = get_game_state()
    state.penalty_time = 0
    state.penalty_running = False
    state.save()
    return redirect('admin_dashboard')


def get_game_state_json(request):
    state = get_game_state()
    return JsonResponse({
        'team_red_name': state.team_red_name,
        'team_blue_name': state.team_blue_name,
        'team_red_score': state.team_red_score,
        'team_blue_score': state.team_blue_score,
        'round_number': state.round_number,
        'game_time': state.game_time,
        'penalty_time': state.penalty_time,
        'game_running': state.game_running,
        'penalty_running': state.penalty_running,
    })


# views.py mein ye function add karo
def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"

# viewer function update karo
def viewer(request):
    state = get_game_state()
    context = {
        'state': state,
        'formatted_game_time': format_time(state.game_time),
        'formatted_penalty_time': format_time(state.penalty_time)
    }
    return render(request, 'viewer.html', context)


# views.py mein top par imports add karo
import threading
import time
from django.utils import timezone

# Global variable for timer thread
timer_thread = None

# Timer thread function
def timer_worker():
    while True:
        try:
            state = GameState.objects.get(id=1)
            state.update_timers()
            time.sleep(1)
        except:
            time.sleep(1)

# Timer thread start function
def start_timer_thread():
    global timer_thread
    if timer_thread is None or not timer_thread.is_alive():
        timer_thread = threading.Thread(target=timer_worker, daemon=True)
        timer_thread.start()

# App ready hone par timer start karne ke liye
# apps.py mein ye code add karo
from django.apps import AppConfig

class ScoreboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scoreboard'
    
    def ready(self):
        start_timer_thread()