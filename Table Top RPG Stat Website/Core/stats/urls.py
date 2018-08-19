from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('player/<int:PID>', views.player, name='player'),
	path('CharacterSheet/<int:CIDin>', views.Character_Sheet, name='CharacterSheet'),
	path('Character/<int:CIDin>', views.Character_Old, name='character'),
	path('group/<int:GIDin>', views.group, name = 'group'),
]