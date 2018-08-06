from django.shortcuts import render

#games models
from .models import Group
from .models import Character

#Show a list of all the groups
def index(request):
	topTenGroups = Group.objects.order_by('GID')[:10]
	context = {'topTenGroups': topTenGroups}
	return render(request, 'stats/index.html', context)

#groups
def group(request, GIDin):
	try:
		chractersInGroup = Character.objects.filter(GID = GIDin)
	except Character.DoesNotExist:
		raise Http404("group does not exist")
	return render(request, 'stats/group.html', {'chractersInGroup': chractersInGroup})

	
#character sheet
def player(request, PID):
	return HttpResponse("You're looking at the chracters of %s." % PID)
	
	
#player characters
def CharacterSheet(request, CIDin):
	try:
		chractersInGroup = Character.objects.filter(CID = CIDin)
	except Character.DoesNotExist:
		raise Http404("character does not exist")
	return render(request, 'stats/character.html', {'chractersInGroup': chractersInGroup})

