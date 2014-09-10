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
	try:
		game = Game.objects.get(pk=gsid)
	except Game.DoesNotExist:
		raise Http404
	return render(request, 'games/detail.html', {'game':game})
