from django import template

register = template.Library()
#<a href="{% url 'player_detail' player.player_id %}">{{player.player.full_name}}</a>

