from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

#games models
from .models import Group
from .models import Character
from .models import character_Access

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

	
#these are the players characters
def player(request, PID):
	return HttpResponse("You're looking at the chracters of %s." % PID)
	
	
#player characters
def CharacterSheet(request, CIDin):
	uname = 'NotLoggedIn'
	Access = False
	if request.user.is_authenticated:
		uname = request.user.get_username()
		#check table for access
		try:
			accessstats = character_Access.objects.filter(username = uname, CID = CIDin)
			if len(accessstats) > 0:
				Access = accessstats[0].HasAccess
				uname  = uname + ' - ' + str(Access)
			else:
				uname = uname +  ' - [not in table]' 
		except Exception as e:
			uname = uname + '[Access Error]' + str(e)
		
	try:
		chractersInGroup = Character.objects.filter(CID = CIDin)
	except Character.DoesNotExist:
		raise Http404("character does not exist")
	if Access:
		return render(request, 'stats/characterCon.html', {'chractersInGroup': chractersInGroup, 'userNamePass': uname})
	else:
		return render(request, 'stats/characterLim.html', {'chractersInGroup': chractersInGroup, 'userNamePass': uname})

