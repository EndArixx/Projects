from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('player/<int:PID>', views.player, name='player'),
	path('CharacterSheet/<int:CIDin>', views.CharacterSheet, name='CharacterSheet'),
	path('group/<int:GIDin>', views.group, name = 'group'),
]