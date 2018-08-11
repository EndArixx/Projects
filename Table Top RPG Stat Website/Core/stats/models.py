from django.db import models

'''
IMPORTANT Identifiers/ForeignKeys:

	PID = Player ID 
	CID = Character ID
	GID = Group ID
	FID = Faction ID
	STID = Stat ID
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
#-------------------------------------------------------------------	
#-------------------------Character Zone----------------------------
#-------------------------------------------------------------------	
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

'''
HP of the player
'''		
class Character_HP(models.Model):
	#Charater ID
	CID = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key = True) 
		#Max allowed HP per slot
	Max_Head_HP = models.IntegerField(default=25)
	Max_Core_HP = models.IntegerField(default=50)
	Max_Right_Arm_HP = models.IntegerField(default=30)
	Max_Left_Arm_HP = models.IntegerField(default=30)
	Max_Right_Leg_HP = models.IntegerField(default=30)
	Max_Left_Leg_HP = models.IntegerField(default=30)
		#Current HP per slot
	Head_HP = models.IntegerField(default=Max_Head_HP.default)
	Core_HP = models.IntegerField(default=Max_Core_HP.default)
	Right_Arm_HP = models.IntegerField(default=Max_Right_Arm_HP.default)
	Left_Arm_HP = models.IntegerField(default=Max_Left_Arm_HP.default)
	Right_Leg_HP = models.IntegerField(default=Max_Right_Leg_HP.default)
	Left_Leg_HP = models.IntegerField(default=Max_Left_Leg_HP.default)
		#Misc
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.CID.Character_Name
	
class character_Access(models.Model):
	username =  models.CharField(max_length=200)
	CID = models.OneToOneField(Character, on_delete=models.CASCADE) 
	HasAccess = models.BooleanField(default = False)
	HasEdit = models.BooleanField(default = False)
	def __str__(self):
		return self.username +' - '+ self.CID.Character_Name

#-------------------------------------------------------------------			
#---------------------------Armor Zone -----------------------------
#-------------------------------------------------------------------	
class Armor(models.Model):
	AID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	Value = models.IntegerField(default=10)
	Special_Feature =  models.CharField(max_length=2000,blank=True, null=True)
	Allow_Head = models.BooleanField(default = True)
	Allow_Core = models.BooleanField(default = True)
	Allow_Right_Arm = models.BooleanField(default = True)
	Allow_Left_Arm = models.BooleanField(default = True)
	Allow_Right_Leg = models.BooleanField(default = True)
	Allow_Left_Leg = models.BooleanField(default = True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name
	
class Character_Equipped_Armor(models.Model):
	CID = models.ForeignKey(Character, on_delete=models.CASCADE) 
	AID = models.ForeignKey(Armor, on_delete=models.CASCADE) 
	Equiped_Head = models.BooleanField(default = True)
	Equiped_Core = models.BooleanField(default = True)
	Equiped_Right_Arm = models.BooleanField(default = True)
	Equiped_Left_Arm = models.BooleanField(default = True)
	Equiped_Right_Leg = models.BooleanField(default = True)
	Equiped_Left_Leg = models.BooleanField(default = True)
	class Meta:
		unique_together = (('CID', 'AID'),)
	def __str__(self):
		return self.CID.Character_Name + ' - '+ self.AID.Name
		
class Character_Equipped_Armor_Value(models.Model):
		#Charater ID
	CID = models.OneToOneField(Character, on_delete=models.CASCADE, primary_key = True) 
		#Max allowed HP per slot
	Max_Head_Armor = models.IntegerField(default=0)
	Max_Core_Armor = models.IntegerField(default=0)
	Max_Right_Arm_Armor = models.IntegerField(default=0)
	Max_Left_Arm_Armor = models.IntegerField(default=0)
	Max_Right_Leg_Armor = models.IntegerField(default=0)
	Max_Left_Leg_Armor = models.IntegerField(default=0)
		#Current HP per slot
	Head_Armor = models.IntegerField(default=Max_Head_Armor.default)
	Core_Armor = models.IntegerField(default=Max_Core_Armor.default)
	Right_Arm_Armor = models.IntegerField(default=Max_Right_Arm_Armor.default)
	Left_Arm_Armor = models.IntegerField(default=Max_Left_Arm_Armor.default)
	Right_Leg_Armor = models.IntegerField(default=Max_Right_Leg_Armor.default)
	Left_Leg_Armor = models.IntegerField(default=Max_Left_Leg_Armor.default)
		#Misc
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.CID.Character_Name

#-------------------------------------------------------------------			
#--------------------------- Weapon Zone ---------------------------
#-------------------------------------------------------------------		

#-------------------------------------------------------------------	
#------------------------------ Skills -----------------------------
#-------------------------------------------------------------------	

class Stat(models.Model):
	STID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200,blank=True, null=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name
		
class Character_Stat(models.Model):
	CID = models.ForeignKey(Character, on_delete=models.CASCADE) 
	STID =  models.ForeignKey(Stat, on_delete=models.CASCADE) 
	Value = models.IntegerField(default=0)
	class Meta:
		unique_together = ('CID', 'STID')
		
	def __str__(self):
		return self.CID.Character_Name + ' - '+ self.STID.Name
	
class Skill(models.Model):
	SID = models.AutoField(primary_key=True)
	STID =  models.ForeignKey(Stat, on_delete=models.CASCADE) 
	Name =  models.CharField(max_length=200,blank=True, null=True)
	Cost = models.IntegerField(default=2)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name
		
class Character_Skill(models.Model):
	CID = models.ForeignKey(Character, on_delete=models.CASCADE) 
	SID = models.ForeignKey(Skill, on_delete=models.CASCADE) 
	Mod = models.IntegerField(default=2)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = ('CID', 'SID')
		
	def __str__(self):
		return self.CID.Character_Name + ' - '+ self.SID.Name

#-------------------------------------------------------------------			
#----------------------------- Item Zone ---------------------------
#-------------------------------------------------------------------

class Item(models.Model):
	IID = models.AutoField(primary_key=True)
	CID = models.ForeignKey(Character, on_delete=models.CASCADE) 
	Name =  models.CharField(max_length=200)
	Count = models.IntegerField(default=1)
	Description =  models.CharField(max_length=2000,blank=True, null=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)

	def __str__(self):
		return self.CID.Character_Name + ' - '+ self.Name

#-------------------------------------------------------------------	
#------------------------------ NPC --------------------------------
#-------------------------------------------------------------------	
		
#-------------------------------------------------------------------	
#----------------------------- MISC --------------------------------
#-------------------------------------------------------------------	
class War_Crime(models.Model):
	War_Crime_ID =  models.AutoField(primary_key=True)
	War_Crime_Name =  models.CharField(max_length=200)
	GID = models.ForeignKey(Group, on_delete=models.CASCADE) 
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.War_Crime_Name	
		
		
		
		
		
		
		
		
		