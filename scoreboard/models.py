from django.db import models

class GameState(models.Model):
    team_red_score = models.IntegerField(default=0)
    team_blue_score = models.IntegerField(default=0)
    round_number = models.IntegerField(default=1)

    game_time = models.IntegerField(default=180)  # in seconds
    game_running = models.BooleanField(default=False)

    penalty_time = models.IntegerField(default=0)
    penalty_running = models.BooleanField(default=False)

    team_red_name = models.CharField(max_length=50, default="Red Team")
    team_blue_name = models.CharField(max_length=50, default="Blue Team")

    def __str__(self):
        return f"Round {self.round_number} | {self.team_red_name} vs {self.team_blue_name}"
