from django.db import models

class Game(models.Model):
	gsis_id=models.CharField(max_length=10,primary_key=True)
	start_time=models.DateTimeField('Game Start Time')
	finished=models.BooleanField()
#Home team data
	home_team=models.CharField(max_length=30)
	home_score=models.SmallIntegerField()
	home_score_Q1=models.SmallIntegerField()
	home_score_Q2=models.SmallIntegerField()
	home_score_Q3=models.SmallIntegerField()
	home_score_Q4=models.SmallIntegerField()
	home_score_Q5=models.SmallIntegerField()
#Away team data
	away_team=models.CharField(max_length=30)
	away_score=models.SmallIntegerField()
	away_score_Q1=models.SmallIntegerField()
	away_score_Q2=models.SmallIntegerField()
	away_score_Q3=models.SmallIntegerField()
	away_score_Q4=models.SmallIntegerField()
	away_score_Q5=models.SmallIntegerField()
