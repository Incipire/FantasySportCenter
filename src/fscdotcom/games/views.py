from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
import nfldb

def index(request,year=0,week=0,season_type='Regular'):
    db = nfldb.connect()
    current=nfldb.current(db)
    if year==0 :
        season_type,year,week=nfldb.current(db)
        return redirect('index',year, season_type.name, week)
    q =nfldb.Query(db).game(season_year=year, season_type=season_type, week=week).sort('start_time')
    games=q.as_games()
    return render(request, 'games/index.html', 
            {'games_list':games, 'current':current, 'year':year})


def player_detail(request, player_id):
    db = nfldb.connect()
    player = nfldb.Player.from_id(db,player_id) 

    if (player is None):
        raise Http404
    player_games= get_player_stats_by_game(player_id,db)
    template=select_player_template(player)
    return render(request, template,
       {'player':player, 'player_games':player_games})


def get_player_stats_by_game(player_id,db):
    #Get the season typ, year, and week
    season_type,year,week=nfldb.current(db)
    q = nfldb.Query(db).player(player_id=player_id)
    games = q.game(season_year=year,season_type=season_type,week__le=week).sort(('week','asc')).as_games()
    player_games=[]
    for game in games:
        agg = nfldb.Query(db).player(player_id=player_id).game(gsis_id=game.gsis_id).as_aggregate()[0]
        pass_avg=0
        rushing_avg=0
        receiving_avg=0
        if (agg.passing_att>0):
          pass_avg=agg.passing_yds/float(agg.passing_att)
        if (agg.rushing_att>0):
          rushing_avg=agg.rushing_yds/float(agg.rushing_att)
        if (agg.receiving_rec>0):
          receiving_avg=agg.receiving_yds/float(agg.receiving_rec)
        player_games.append({'player':agg,'game':game,'pass_avg':pass_avg, 'rushing_avg':rushing_avg, 'receiving_avg':receiving_avg})
    return player_games

def select_player_template(player):
    template = 'games/player_detail.html'
    if(str(player.position)=='WR'):
        template= 'games/player_wr_detail.html'
    if(str(player.position)=='RB'):
        template='games/player_rb_detail.html'
    return template

def detail(request, gsid):
    db = nfldb.connect()
    q = nfldb.Query(db).game(gsis_id=gsid)
    games=q.as_games()
    if (len(games)!=1):
        raise Http404
    game = games[0] 
    year=game.season_year
    week=game.week
    season_type=game.season_type
    games =nfldb.Query(db).game(season_year=year, season_type=season_type, week=week).sort('start_time').as_games() 
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
                'games':games,
                })
