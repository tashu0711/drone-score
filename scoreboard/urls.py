from django.urls import path
from . import views

urlpatterns = [
    path("viewer/", views.viewer, name="viewer"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("increment-score/<str:team>/", views.increment_score, name="increment_score"),
    path("decrement-score/<str:team>/", views.decrement_score, name="decrement_score"),
    path("next-round/", views.next_round, name="next_round"),
    path("reset-timer/", views.reset_timer, name="reset_timer"),
    path("toggle-timer/", views.toggle_timer, name="toggle_timer"),
    path("reset-penalty/", views.reset_penalty, name="reset_penalty"),
    path("get-game-state-json/", views.get_game_state_json, name="get_game_state_json"),
]


