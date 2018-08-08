from django.db import models

'''
IMPORTANT Identifiers/ForeignKeys:

	PID = Player ID 
	CID = Character ID
	GID = Group ID
	FID = Faction ID
	SID = Skill ID
	--items--
	WID = Weapon ID
	AID = Armor ID
	IIP = Item ID
	BID = Ammo ID
	--tank--
	TUID = Tank Upgrade ID
'''


'''
This is the ID of the Actually player, this is used when the player logs in.
'''
class Player(models.Model):
	player_name = models.CharField(max_length=200)
	PID = models.AutoField(primary_key=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.player_name

'''
This is a group or Party of charactesr that are currenlty playing a campaign. 
You can think of group as a campaign.

JOHN what happens if a player is in more than one group?
'''
class Group(models.Model):
	Group_name = models.CharField(max_length=200)
	GID = models.AutoField(primary_key=True)
	#JOHN add FID  FK nullable
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Group_name
	
'''
These are specific charcters each character must have a Group and a player. 

JOHN is it possible for a player to have mutiple characters in the same Group?
'''
class Character(models.Model):
	#names_And FKs
	CID = models.AutoField(primary_key=True)
	Character_Name =  models.CharField(max_length=200)
	PID = models.ForeignKey(Player, on_delete=models.CASCADE) 
	GID = models.ForeignKey(Group, on_delete=models.CASCADE) 
	Character_Image  =  models.CharField(max_length=200, blank=True, null=True)
	#stats
	MIND_stat = models.IntegerField(default=0)
	FIST_stat = models.IntegerField(default=0)
	EYES_stat = models.IntegerField(default=0)
	FACE_stat = models.IntegerField(default=0)
	HEART_stat = models.IntegerField(default=0)
	MaxActionSurges_stat = models.IntegerField(default=5)
	TotalActionSurges_stat = models.IntegerField(default=0)
	ActionSurges_stat = models.IntegerField(default=0)
	Weakness_failed_stat = models.IntegerField(default=0)
	Weakness_passed_stat = models.IntegerField(default=0)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Character_Name

		
class Character_HP(models.Model):
	#Charater ID
	CID = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key = True) 
	#Max allowed HP per slot
	MAX_Head_HP = models.IntegerField(default=25)
	Max_Core_HP = models.IntegerField(default=50)
	Max_Right_Arm_HP = models.IntegerField(default=30)
	Max_Left_Arm_HP = models.IntegerField(default=30)
	Max_Right_Leg_HP = models.IntegerField(default=30)
	Max_Left_Leg_HP = models.IntegerField(default=30)
	
	#Current HP per slot
	Head_HP = models.IntegerField(default=MAX_Head_HP.default)
	Core_HP = models.IntegerField(default=Max_Core_HP.default)
	Right_Arm_HP = models.IntegerField(default=Max_Right_Arm_HP.default)
	Left_Arm_HP = models.IntegerField(default=Max_Left_Arm_HP.default)
	Right_Leg_HP = models.IntegerField(default=Max_Right_Leg_HP.default)
	Left_Leg_HP = models.IntegerField(default=Max_Left_Leg_HP.default)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.CID.Character_Name
	
class War_Crime(models.Model):
	War_Crime_ID =  models.AutoField(primary_key=True)
	War_Crime_Name =  models.CharField(max_length=200)
	GID = models.ForeignKey(Group, on_delete=models.CASCADE) 
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.War_Crime_Name
	
	
class character_Access(models.Model):
	username =  models.CharField(max_length=200)
	CID = models.OneToOneField(Character, on_delete=models.CASCADE) 
	HasAccess = models.BooleanField(default = False)
	HasEdit = models.BooleanField(default = False)
	def __str__(self):
		return self.username +' - '+ self.CID.Character_Name