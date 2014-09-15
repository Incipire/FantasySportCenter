from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
import nfldb
from models import Game,Meta

def index(request,year=0,week=0,season_type='Regular'):
    db = nfldb.connect()
    current=nfldb.current(db)
    if year==0 :
        year =current[1]
        week = current[2]
        season_type = current[0]
        return redirect('index',year, season_type.name, week)
    q =nfldb.Query(db).game(season_year=year, season_type=season_type, week=week) 
    games=q.as_games()
    #games=Game.objects.filter(season_year=2014).filter(week=1).filter(season_type='Regular')
    return render(request, 'games/index.html', 
            {'games_list':games, 'current':current, 'year':year})


def detail(request, gsid):
    db = nfldb.connect()
    q = nfldb.Query(db).game(gsis_id=gsid)
    games=q.as_games()
    if (len(games)!=1):
        raise Http404
    game = games[0] 
    q.player(team=game.away_team)
    away_pass=q.aggregate(passing_att__gt = 0).sort('passing_yds').as_aggregate()
    home_pass=nfldb.Query(db).game(gsis_id=gsid).player(team=game.home_team).aggregate(passing_att__gt = 0).sort('passing_yds').as_aggregate()
    home_rec=nfldb.Query(db).game(gsis_id=gsid).player(team=game.home_team).aggregate(receiving_rec__gt = 0).sort('receiving_yds').as_aggregate()
    away_rec=nfldb.Query(db).game(gsis_id=gsid).player(team=game.away_team).aggregate(receiving_rec__gt = 0).sort('receiving_yds').as_aggregate()
    away_run=nfldb.Query(db).game(gsis_id=gsid).player(team=game.away_team).aggregate(rushing_att__gt = 0).sort('rushing_yds').as_aggregate()
    home_run=nfldb.Query(db).game(gsis_id=gsid).player(team=game.home_team).aggregate(rushing_att__gt = 0).sort('rushing_yds').as_aggregate()
    return render(request, 'games/detail.html', 
            {'game':game, 
                'away_run':away_run,
                'home_run':home_run,
                'away_pass':away_pass, 
                'home_pass':home_pass,
                'home_rec':home_rec,
                'away_rec':away_rec,
                })
