from django.shortcuts import get_object_or_404,render
from django.contrib.auth.decorators import permission_required
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.staticfiles import finders

#models
from .models import  *

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

	
#player Character Sheet	
def Character_Sheet(request, CIDin):
	uname = 'NotLoggedIn'
	Access = False
	
	#check access rights of user.
	if request.user.is_authenticated:
		uname = request.user.get_username()
		try:
			#Get player Name
			playA = Player.objects.get(Name = uname)
			PIDin = playA.PID
			accessstats = character_Access.objects.get(PID = PIDin, CID = CIDin)
			if accessstats != None:
				Access = accessstats.HasAccess
				uname  = uname + ' - ' + str(Access)
			else:
				uname = uname +  ' - [not in table]' 
		except Exception as e:
			uname = uname + '[Access Error]' + str(e)
		
	character = get_object_or_404(Character,CID = CIDin)
		
	try:
		#getHP/Armour Data		
		characterHP = get_object_or_404(Character_HP,CID = CIDin)	
		#john this is dirty
		characterArmor = Character_Equipped_Armor_Value.objects.filter(CID = CIDin).first()
		characterStatus = Character_Status.objects.filter(CID = CIDin, Hidden = False)
		
		#team members
		groupMembers = Character.objects.filter(GID = character.GID)
	
		#stats
		characterStat = Character_Stat.objects.filter(CID = CIDin)	
		characterSkill = Character_Skill.objects.filter(CID = CIDin)	
		characterPower = Character_Power.objects.filter(CID = CIDin, Hidden = False)	

		#Items
		characterWeapon = Character_Weapon.objects.filter(CID = CIDin, Hidden = False)	
		characterGear = Character_Item.objects.filter(CID = CIDin, Equipable = True, Hidden = False)	
		characterItem = Character_Item.objects.filter(CID = CIDin, Equipable = False, Hidden = False)	
		
		characterDetails = Character_Details.objects.filter(CID = CIDin, Hidden = False)	
		
		if not character.Image:		
			character.Image = 'default.png'
		else:
			image = finders.find('stats/character/'+character.Image)
			if not image:
				character.Image = 'invalid.png'
			
		
	except Exception as e:
		print(str(e))
		raise Http404("Error loading character: " + str(character.Name))

	return render(request, 'stats/CharacterNewLim.html', {
	'character': character,
	'characterHP': characterHP,
	'characterArmor': characterArmor,
	'groupMembers': groupMembers,
	'characterStat': characterStat,
	'characterSkill': characterSkill,
	'characterPower': characterPower,
	'characterWeapon': characterWeapon,
	'characterGear': characterGear,
	'characterItem': characterItem,
	'characterDetails': characterDetails,
	'characterStatus': characterStatus,
	'userNamePass': uname})	
	
	
#JOHN USED FOR TESTING YOU MAY REMOVE AFTER NEW SHEETS ARE COMPLETED
#player characters
def Character_Old(request, CIDin):
	uname = 'NotLoggedIn'
	Access = False
	
	#check access rights of user.
	if request.user.is_authenticated:
		uname = request.user.get_username()
		try:
			#Get player Name
			playA = Player.objects.get(Name = uname)
			PIDin = playA.PID
			accessstats = character_Access.objects.get(PID = PIDin, CID = CIDin)
			if accessstats != None:
				Access = accessstats.HasAccess
				uname  = uname + ' - ' + str(Access)
			else:
				uname = uname +  ' - [not in table]' 
		except Character.DoesNotExist:
			raise Http404("Character does not exist")
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
		
		
