# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AggPlay(models.Model):
    gsis = models.ForeignKey('Game')
    drive_id = models.SmallIntegerField()
    play_id = models.SmallIntegerField()
    defense_ast = models.SmallIntegerField()
    defense_ffum = models.SmallIntegerField()
    defense_fgblk = models.SmallIntegerField()
    defense_frec = models.SmallIntegerField()
    defense_frec_tds = models.SmallIntegerField()
    defense_frec_yds = models.SmallIntegerField()
    defense_int = models.SmallIntegerField()
    defense_int_tds = models.SmallIntegerField()
    defense_int_yds = models.SmallIntegerField()
    defense_misc_tds = models.SmallIntegerField()
    defense_misc_yds = models.SmallIntegerField()
    defense_pass_def = models.SmallIntegerField()
    defense_puntblk = models.SmallIntegerField()
    defense_qbhit = models.SmallIntegerField()
    defense_safe = models.SmallIntegerField()
    defense_sk = models.FloatField()
    defense_sk_yds = models.SmallIntegerField()
    defense_tkl = models.SmallIntegerField()
    defense_tkl_loss = models.SmallIntegerField()
    defense_tkl_loss_yds = models.SmallIntegerField()
    defense_tkl_primary = models.SmallIntegerField()
    defense_xpblk = models.SmallIntegerField()
    fumbles_forced = models.SmallIntegerField()
    fumbles_lost = models.SmallIntegerField()
    fumbles_notforced = models.SmallIntegerField()
    fumbles_oob = models.SmallIntegerField()
    fumbles_rec = models.SmallIntegerField()
    fumbles_rec_tds = models.SmallIntegerField()
    fumbles_rec_yds = models.SmallIntegerField()
    fumbles_tot = models.SmallIntegerField()
    kicking_all_yds = models.SmallIntegerField()
    kicking_downed = models.SmallIntegerField()
    kicking_fga = models.SmallIntegerField()
    kicking_fgb = models.SmallIntegerField()
    kicking_fgm = models.SmallIntegerField()
    kicking_fgm_yds = models.SmallIntegerField()
    kicking_fgmissed = models.SmallIntegerField()
    kicking_fgmissed_yds = models.SmallIntegerField()
    kicking_i20 = models.SmallIntegerField()
    kicking_rec = models.SmallIntegerField()
    kicking_rec_tds = models.SmallIntegerField()
    kicking_tot = models.SmallIntegerField()
    kicking_touchback = models.SmallIntegerField()
    kicking_xpa = models.SmallIntegerField()
    kicking_xpb = models.SmallIntegerField()
    kicking_xpmade = models.SmallIntegerField()
    kicking_xpmissed = models.SmallIntegerField()
    kicking_yds = models.SmallIntegerField()
    kickret_fair = models.SmallIntegerField()
    kickret_oob = models.SmallIntegerField()
    kickret_ret = models.SmallIntegerField()
    kickret_tds = models.SmallIntegerField()
    kickret_touchback = models.SmallIntegerField()
    kickret_yds = models.SmallIntegerField()
    passing_att = models.SmallIntegerField()
    passing_cmp = models.SmallIntegerField()
    passing_cmp_air_yds = models.SmallIntegerField()
    passing_incmp = models.SmallIntegerField()
    passing_incmp_air_yds = models.SmallIntegerField()
    passing_int = models.SmallIntegerField()
    passing_sk = models.SmallIntegerField()
    passing_sk_yds = models.SmallIntegerField()
    passing_tds = models.SmallIntegerField()
    passing_twopta = models.SmallIntegerField()
    passing_twoptm = models.SmallIntegerField()
    passing_twoptmissed = models.SmallIntegerField()
    passing_yds = models.SmallIntegerField()
    punting_blk = models.SmallIntegerField()
    punting_i20 = models.SmallIntegerField()
    punting_tot = models.SmallIntegerField()
    punting_touchback = models.SmallIntegerField()
    punting_yds = models.SmallIntegerField()
    puntret_downed = models.SmallIntegerField()
    puntret_fair = models.SmallIntegerField()
    puntret_oob = models.SmallIntegerField()
    puntret_tds = models.SmallIntegerField()
    puntret_tot = models.SmallIntegerField()
    puntret_touchback = models.SmallIntegerField()
    puntret_yds = models.SmallIntegerField()
    receiving_rec = models.SmallIntegerField()
    receiving_tar = models.SmallIntegerField()
    receiving_tds = models.SmallIntegerField()
    receiving_twopta = models.SmallIntegerField()
    receiving_twoptm = models.SmallIntegerField()
    receiving_twoptmissed = models.SmallIntegerField()
    receiving_yac_yds = models.SmallIntegerField()
    receiving_yds = models.SmallIntegerField()
    rushing_att = models.SmallIntegerField()
    rushing_loss = models.SmallIntegerField()
    rushing_loss_yds = models.SmallIntegerField()
    rushing_tds = models.SmallIntegerField()
    rushing_twopta = models.SmallIntegerField()
    rushing_twoptm = models.SmallIntegerField()
    rushing_twoptmissed = models.SmallIntegerField()
    rushing_yds = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'agg_play'

class Drive(models.Model):
    gsis = models.ForeignKey('Game')
    drive_id = models.SmallIntegerField()
    start_field = models.TextField(blank=True) # This field type is a guess.
    start_time = models.TextField() # This field type is a guess.
    end_field = models.TextField(blank=True) # This field type is a guess.
    end_time = models.TextField() # This field type is a guess.
    pos_team = models.ForeignKey('Team', db_column='pos_team')
    pos_time = models.TextField(blank=True) # This field type is a guess.
    first_downs = models.SmallIntegerField()
    result = models.TextField(blank=True)
    penalty_yards = models.SmallIntegerField()
    yards_gained = models.SmallIntegerField()
    play_count = models.SmallIntegerField()
    time_inserted = models.DateTimeField()
    time_updated = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'drive'

class Game(models.Model):
    gsis_id = models.CharField(primary_key=True, max_length=10)
    gamekey = models.CharField(max_length=5, blank=True)
    start_time = models.DateTimeField()
    week = models.SmallIntegerField()
    day_of_week = models.TextField() # This field type is a guess.
    season_year = models.SmallIntegerField()
    season_type = models.TextField() # This field type is a guess.
    finished = models.BooleanField()
    home_team = models.ForeignKey('Team', db_column='home_team', related_name='home_games')
    home_score = models.SmallIntegerField()
    home_score_q1 = models.SmallIntegerField(blank=True, null=True)
    home_score_q2 = models.SmallIntegerField(blank=True, null=True)
    home_score_q3 = models.SmallIntegerField(blank=True, null=True)
    home_score_q4 = models.SmallIntegerField(blank=True, null=True)
    home_score_q5 = models.SmallIntegerField(blank=True, null=True)
    home_turnovers = models.SmallIntegerField()
    away_team = models.ForeignKey('Team', db_column='away_team', related_name='away_games')
    away_score = models.SmallIntegerField()
    away_score_q1 = models.SmallIntegerField(blank=True, null=True)
    away_score_q2 = models.SmallIntegerField(blank=True, null=True)
    away_score_q3 = models.SmallIntegerField(blank=True, null=True)
    away_score_q4 = models.SmallIntegerField(blank=True, null=True)
    away_score_q5 = models.SmallIntegerField(blank=True, null=True)
    away_turnovers = models.SmallIntegerField()
    time_inserted = models.DateTimeField()
    time_updated = models.DateTimeField()
    def __unicode__(self):
	    return "{}({}) vs. {}({})".format(
			    self.home_team,
			    self.home_score,
			    self.away_team,
			    self.away_score,
			    ) 
    class Meta:
        managed = False
        db_table = 'game'

class Meta(models.Model):
    version = models.SmallIntegerField(blank=True, null=True)
    last_roster_download = models.DateTimeField()
    season_type = models.TextField(blank=True) # This field type is a guess.
    season_year = models.SmallIntegerField(blank=True, null=True)
    week = models.SmallIntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'meta'

class Play(models.Model):
    gsis = models.ForeignKey(Game)
    drive_id = models.SmallIntegerField()
    play_id = models.SmallIntegerField()
    time = models.TextField() # This field type is a guess.
    pos_team = models.ForeignKey('Team', db_column='pos_team')
    yardline = models.TextField(blank=True) # This field type is a guess.
    down = models.SmallIntegerField(blank=True, null=True)
    yards_to_go = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)
    time_inserted = models.DateTimeField()
    time_updated = models.DateTimeField()
    first_down = models.SmallIntegerField()
    fourth_down_att = models.SmallIntegerField()
    fourth_down_conv = models.SmallIntegerField()
    fourth_down_failed = models.SmallIntegerField()
    passing_first_down = models.SmallIntegerField()
    penalty = models.SmallIntegerField()
    penalty_first_down = models.SmallIntegerField()
    penalty_yds = models.SmallIntegerField()
    rushing_first_down = models.SmallIntegerField()
    third_down_att = models.SmallIntegerField()
    third_down_conv = models.SmallIntegerField()
    third_down_failed = models.SmallIntegerField()
    timeout = models.SmallIntegerField()
    xp_aborted = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'play'

class PlayPlayer(models.Model):
    gsis = models.ForeignKey(Game)
    drive_id = models.SmallIntegerField()
    play_id = models.SmallIntegerField()
    player = models.ForeignKey('Player')
    team = models.ForeignKey('Team', db_column='team')
    defense_ast = models.SmallIntegerField()
    defense_ffum = models.SmallIntegerField()
    defense_fgblk = models.SmallIntegerField()
    defense_frec = models.SmallIntegerField()
    defense_frec_tds = models.SmallIntegerField()
    defense_frec_yds = models.SmallIntegerField()
    defense_int = models.SmallIntegerField()
    defense_int_tds = models.SmallIntegerField()
    defense_int_yds = models.SmallIntegerField()
    defense_misc_tds = models.SmallIntegerField()
    defense_misc_yds = models.SmallIntegerField()
    defense_pass_def = models.SmallIntegerField()
    defense_puntblk = models.SmallIntegerField()
    defense_qbhit = models.SmallIntegerField()
    defense_safe = models.SmallIntegerField()
    defense_sk = models.FloatField()
    defense_sk_yds = models.SmallIntegerField()
    defense_tkl = models.SmallIntegerField()
    defense_tkl_loss = models.SmallIntegerField()
    defense_tkl_loss_yds = models.SmallIntegerField()
    defense_tkl_primary = models.SmallIntegerField()
    defense_xpblk = models.SmallIntegerField()
    fumbles_forced = models.SmallIntegerField()
    fumbles_lost = models.SmallIntegerField()
    fumbles_notforced = models.SmallIntegerField()
    fumbles_oob = models.SmallIntegerField()
    fumbles_rec = models.SmallIntegerField()
    fumbles_rec_tds = models.SmallIntegerField()
    fumbles_rec_yds = models.SmallIntegerField()
    fumbles_tot = models.SmallIntegerField()
    kicking_all_yds = models.SmallIntegerField()
    kicking_downed = models.SmallIntegerField()
    kicking_fga = models.SmallIntegerField()
    kicking_fgb = models.SmallIntegerField()
    kicking_fgm = models.SmallIntegerField()
    kicking_fgm_yds = models.SmallIntegerField()
    kicking_fgmissed = models.SmallIntegerField()
    kicking_fgmissed_yds = models.SmallIntegerField()
    kicking_i20 = models.SmallIntegerField()
    kicking_rec = models.SmallIntegerField()
    kicking_rec_tds = models.SmallIntegerField()
    kicking_tot = models.SmallIntegerField()
    kicking_touchback = models.SmallIntegerField()
    kicking_xpa = models.SmallIntegerField()
    kicking_xpb = models.SmallIntegerField()
    kicking_xpmade = models.SmallIntegerField()
    kicking_xpmissed = models.SmallIntegerField()
    kicking_yds = models.SmallIntegerField()
    kickret_fair = models.SmallIntegerField()
    kickret_oob = models.SmallIntegerField()
    kickret_ret = models.SmallIntegerField()
    kickret_tds = models.SmallIntegerField()
    kickret_touchback = models.SmallIntegerField()
    kickret_yds = models.SmallIntegerField()
    passing_att = models.SmallIntegerField()
    passing_cmp = models.SmallIntegerField()
    passing_cmp_air_yds = models.SmallIntegerField()
    passing_incmp = models.SmallIntegerField()
    passing_incmp_air_yds = models.SmallIntegerField()
    passing_int = models.SmallIntegerField()
    passing_sk = models.SmallIntegerField()
    passing_sk_yds = models.SmallIntegerField()
    passing_tds = models.SmallIntegerField()
    passing_twopta = models.SmallIntegerField()
    passing_twoptm = models.SmallIntegerField()
    passing_twoptmissed = models.SmallIntegerField()
    passing_yds = models.SmallIntegerField()
    punting_blk = models.SmallIntegerField()
    punting_i20 = models.SmallIntegerField()
    punting_tot = models.SmallIntegerField()
    punting_touchback = models.SmallIntegerField()
    punting_yds = models.SmallIntegerField()
    puntret_downed = models.SmallIntegerField()
    puntret_fair = models.SmallIntegerField()
    puntret_oob = models.SmallIntegerField()
    puntret_tds = models.SmallIntegerField()
    puntret_tot = models.SmallIntegerField()
    puntret_touchback = models.SmallIntegerField()
    puntret_yds = models.SmallIntegerField()
    receiving_rec = models.SmallIntegerField()
    receiving_tar = models.SmallIntegerField()
    receiving_tds = models.SmallIntegerField()
    receiving_twopta = models.SmallIntegerField()
    receiving_twoptm = models.SmallIntegerField()
    receiving_twoptmissed = models.SmallIntegerField()
    receiving_yac_yds = models.SmallIntegerField()
    receiving_yds = models.SmallIntegerField()
    rushing_att = models.SmallIntegerField()
    rushing_loss = models.SmallIntegerField()
    rushing_loss_yds = models.SmallIntegerField()
    rushing_tds = models.SmallIntegerField()
    rushing_twopta = models.SmallIntegerField()
    rushing_twoptm = models.SmallIntegerField()
    rushing_twoptmissed = models.SmallIntegerField()
    rushing_yds = models.SmallIntegerField()
    class Meta:
        managed = False
        db_table = 'play_player'

class Player(models.Model):
    player_id = models.CharField(primary_key=True, max_length=10)
    gsis_name = models.CharField(max_length=75, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    team = models.ForeignKey('Team', db_column='team')
    position = models.TextField() # This field type is a guess.
    profile_id = models.IntegerField(blank=True, null=True)
    profile_url = models.CharField(max_length=255, blank=True)
    uniform_number = models.SmallIntegerField(blank=True, null=True)
    birthdate = models.CharField(max_length=75, blank=True)
    college = models.CharField(max_length=255, blank=True)
    height = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    years_pro = models.SmallIntegerField(blank=True, null=True)
    status = models.TextField() # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'player'

class Team(models.Model):
    team_id = models.CharField(primary_key=True, max_length=3)
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    def __unicode__(self):
	    return "{} {}".format(self.city,self.name)
    class Meta:
        managed = False
        db_table = 'team'

