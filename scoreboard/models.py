from django.db import models

class GameState(models.Model):
    team_red_name = models.CharField(max_length=100, default="Team Red")
    team_blue_name = models.CharField(max_length=100, default="Team Blue")
    team_red_score = models.IntegerField(default=0)
    team_blue_score = models.IntegerField(default=0)
    round_number = models.IntegerField(default=1)
    game_time = models.IntegerField(default=180)  # 3 minutes in seconds
    penalty_time = models.IntegerField(default=0)
    game_running = models.BooleanField(default=False)
    penalty_running = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Game State - Round {self.round_number}"
    
    # models.py mein GameState class ke andar ye method add karo
    def update_timers(self):
        if self.game_running and self.game_time > 0:
            self.game_time -= 1
        if self.penalty_running and self.penalty_time > 0:
            self.penalty_time -= 1
        self.save()