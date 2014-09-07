from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from models import Game

def index(request):
	games=Game.objects.filter(season_year=2014).filter(week=1).filter(season_type='Regular')
	context = RequestContext(request, {
		})
	return render(request, 'games/index.html', 
			{'games_list':games})


def detail(request, gsid):
	try:
		game = Game.objects.get(pk=gsid)
	except Game.DoesNotExist:
		raise Http404
	return render(request, 'games/detail.html', {'game':game})
