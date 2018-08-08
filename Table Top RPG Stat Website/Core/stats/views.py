from django.shortcuts import get_object_or_404,render
from django.contrib.auth.decorators import permission_required
#needed?
from django.http import HttpResponseRedirect

#models
from .models import Group
from .models import Character
from .models import Character_HP
from .models import character_Access

#forms
from .forms import CharacterForm

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
	
	#check access rights of user.
	if request.user.is_authenticated:
		uname = request.user.get_username()
		#check table for access
		try:
			accessstats = character_Access.objects.get(username = uname, CID = CIDin)
			if accessstats != None:
				Access = accessstats.HasAccess
				uname  = uname + ' - ' + str(Access)
			else:
				uname = uname +  ' - [not in table]' 
		except Character.DoesNotExist:
			raise Http404("group does not exist")
		except Exception as e:
			uname = uname + '[Access Error]' + str(e)
		
	try:
		chractersInGroup = Character.objects.get(CID = CIDin)
	except  Character.DoesNotExist:
		raise Http404("character does not exist")
		
	if Access:
		#getHP Data		
		characterHP = get_object_or_404(Character_HP,CID = CIDin)
		#JOHN: this should have a new method
		if request.method == 'POST':
			form = CharacterForm(request.POST)
			#user is updating?
			if form.is_valid():
				if form.cleaned_data['MIND_stat_f'] != None:
					chractersInGroup.MIND_stat = form.cleaned_data['MIND_stat_f']
					
				if form.cleaned_data['FIST_stat_f'] != None:
					chractersInGroup.FIST_stat = form.cleaned_data['FIST_stat_f']
					
				if form.cleaned_data['EYES_stat_f'] != None:
					chractersInGroup.EYES_stat = form.cleaned_data['EYES_stat_f']
					
				if form.cleaned_data['FACE_stat_f'] != None:
					chractersInGroup.FACE_stat = form.cleaned_data['FACE_stat_f']
					
				if form.cleaned_data['HEART_stat_f'] != None:
					chractersInGroup.HEART_stat = form.cleaned_data['HEART_stat_f']
				chractersInGroup.save()
				
		else:
			form = CharacterForm()
		#Send Access
		return render(request, 'stats/characterCon.html', {'chractersInGroup': chractersInGroup,'characterHP': characterHP, 'userNamePass': uname, 'form': form})
	else:
		#send Non Access
		return render(request, 'stats/characterLim.html', {'chractersInGroup': chractersInGroup, 'userNamePass': uname})
		
		
