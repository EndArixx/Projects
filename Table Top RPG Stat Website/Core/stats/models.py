from django.db import models

'''
IMPORTANT Identifiers/ForeignKeys:
	--character--
	PID = Player ID 
	CID = Character ID
	GID = Group ID
	SID = Skill ID
	STID = Stat ID
	SUID = Status ID
	--Items--
	WID = Weapon ID
	RIP = Range ID 
	AMID = Ammo ID
	AID = Armor ID
	IIP = Item ID
	BID = Ammo ID
	VID = Vehicle ID
	--NPS--
	NID = NPC ID 
	FID = Faction ID
	WCID = War Crime ID
'''


'''
This is the ID of the Actually player, this is used when the player logs in.
'''

#JOHN LOOK INTO IMPORTING USER FOR PLAYER TABLE


#------------------------------------------------------------------------------	
#----------------------------- Player------------------------------------------
#------------------------------------------------------------------------------	

class Player(models.Model):
	PID = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=200)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name

		
class Faction(models.Model):
	FID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	Image  =  models.CharField(max_length=200, blank=True, null=True)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name
				
		
class Group(models.Model):
	GID = models.AutoField(primary_key=True)
	FID = models.ForeignKey(Faction, on_delete=models.CASCADE) 
	Name = models.CharField(max_length=200)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name
	
		
#------------------------------------------------------------------------------	
#---------------------------- Character ---------------------------------------
#------------------------------------------------------------------------------	

class Character(models.Model):
	#names_And FKs
	CID = models.AutoField(primary_key=True)
	PID = models.ForeignKey(Player, on_delete=models.CASCADE) 
	GID = models.ForeignKey(Group, on_delete=models.CASCADE) 
	Name =  models.CharField(max_length=200)
	Image  =  models.CharField(max_length=200, blank=True, null=True)
	#stats 
	#JOHN REMOVE DIS
	MIND_stat = models.IntegerField(default=0)
	FIST_stat = models.IntegerField(default=0)
	EYES_stat = models.IntegerField(default=0)
	FACE_stat = models.IntegerField(default=0)
	HEART_stat = models.IntegerField(default=0)
	Max_ActionSurges_stat = models.IntegerField(default=5)
	Total_ActionSurges_stat = models.IntegerField(default=0)
	ActionSurges_stat = models.IntegerField(default=0)
	Weakness_failed_stat = models.IntegerField(default=0)
	Weakness_passed_stat = models.IntegerField(default=0)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name

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
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.CID.Name

#------------------------------------------------------------------------------			
#----------------------------- Armor ------------------------------------------
#------------------------------------------------------------------------------	
class Armor(models.Model):
	AID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	Value = models.IntegerField(default=10)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
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
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = (('CID', 'AID'),)
	def __str__(self):
		return self.CID.Name + ' - '+ self.AID.Name
		
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
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.CID.Name

#------------------------------------------------------------------------------			
#------------------------------ Weapon ----------------------------------------
#------------------------------------------------------------------------------		

class Weapon_Range(models.Model):
	RID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name

class Weapon_Ammo(models.Model):
	AAID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name
		
class Weapon(models.Model):
	WID = models.AutoField(primary_key=True)
	RID = models.ForeignKey(Weapon_Range, on_delete=models.CASCADE) 
	AAID  = models.ForeignKey(Weapon_Ammo, on_delete=models.CASCADE) 
	Name =  models.CharField(max_length=200)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	Capacity = models.IntegerField(default=1)
	Rarity  = models.IntegerField(default=1)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.CID.Name + ' - '+ self.Name
		
class Weapon_Character(models.Model):
	CID = models.ForeignKey(Character, on_delete=models.CASCADE) 
	WID = models.ForeignKey(Weapon, on_delete=models.CASCADE) 
	Count = models.IntegerField(default=1)
	Equiped = models.BooleanField(default = False)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = ('CID', 'WID')
	def __str__(self):
		return self.CID.Name + ' - '+ self.WID.Name
	

#------------------------------------------------------------------------------	
#-------------------------- Stats & Skills ------------------------------------
#------------------------------------------------------------------------------	

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
		return self.CID.Name + ' - '+ self.STID.Name
	
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
	Mod = models.IntegerField(default=4)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = ('CID', 'SID')
	def __str__(self):
		return self.CID.Name + ' - '+ self.SID.Name

class Character_Meta(models.Model):
	CID = models.ForeignKey(Character, on_delete=models.CASCADE) 
	Name =  models.CharField(max_length=200,blank=True, null=True)
	Meta_stat =  models.IntegerField(default=0)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	Hidden = models.BooleanField(default = False)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.CID.Name + ' - '+ self.Name
		
#------------------------------------------------------------------------------			
#-------------------------------- Item ----------------------------------------
#------------------------------------------------------------------------------

class Item(models.Model):
	IID = models.AutoField(primary_key=True)
	CID = models.ForeignKey(Character, on_delete=models.CASCADE) 
	Name =  models.CharField(max_length=200)
	Count = models.IntegerField(default=1)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	Equipable = models.BooleanField(default = False)
	Equiped = models.BooleanField(default = False)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.CID.Name + ' - '+ self.Name


class Vehicle(models.Model):
	VID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	functional = models.BooleanField(default = False)
	Max_HP = models.IntegerField(default=100)
	HP = models.IntegerField(default=100)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.Name
		
class Vehicle_Upgrade(models.Model):
	VID = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	GID = models.ForeignKey(Group, on_delete=models.CASCADE)
	Name =  models.CharField(max_length=200)
	Count = models.IntegerField(default=1)
	Equiped = models.BooleanField(default = False)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = ('VID', 'GID')
	def __str__(self):
		return self.GID.Name + ' - '+ self.Name
	
#------------------------------------------------------------------------------			
#------------------------------ Status ----------------------------------------
#------------------------------------------------------------------------------
		
class Status(models.Model):
	SUID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		verbose_name = 'Status'
		verbose_name_plural = 'Statuses'
	def __str__(self):
		return self.Name
		
class Character_Status(models.Model):
	SUID = models.ForeignKey(Status, on_delete=models.CASCADE) 
	CID = models.ForeignKey(Character, on_delete=models.CASCADE)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = ('CID', 'SUID')
	def __str__(self):
		return self.Name

class Vehicle_Status(models.Model):
	SUID = models.ForeignKey(Status, on_delete=models.CASCADE) 
	VID = models.ForeignKey(Character, on_delete=models.CASCADE)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = ('VID', 'SUID')
		verbose_name_plural = 'Vehicle_statuses'
	def __str__(self):
		return self.Name
#------------------------------------------------------------------------------			
#-------------------------------- NPC -----------------------------------------
#------------------------------------------------------------------------------	
		
class NPC(models.Model):
	NID = models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	Image  =  models.CharField(max_length=200, blank=True, null=True)
	Alive = models.BooleanField(default = True)
	Status = models.ForeignKey(Status, on_delete=models.CASCADE)
	FID = models.ForeignKey(Faction, on_delete=models.CASCADE) 
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		verbose_name = 'NPC'
		verbose_name_plural = 'NPCs'
	def __str__(self):
		return self.Name
	
class NPC_Disposition(models.Model):
		#This shows if the NPC likes the player group
	NID = models.ForeignKey(NPC, on_delete=models.CASCADE)
	GID = models.ForeignKey(Group, on_delete=models.CASCADE)
	Disposition = models.IntegerField(default=0)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = ('NID', 'GID')
		verbose_name = 'NPC_Disposition'
		verbose_name_plural = 'NPC_Dispositions'
	def __str__(self):
		return self.NID.Name + ' - '+ self.GID.Name
	
#------------------------------------------------------------------------------	
#----------------------------- MISC -------------------------------------------
#------------------------------------------------------------------------------
	
class War_Crime(models.Model):
	WCID =  models.AutoField(primary_key=True)
	Name =  models.CharField(max_length=200)
	GID = models.ForeignKey(Group, on_delete=models.CASCADE)
	Details =  models.CharField(max_length=2000,blank=True, null=True)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	def __str__(self):
		return self.War_Crime_Name		
		
#------------------------------------------------------------------------------	
#----------------------- Administraction --------------------------------------
#------------------------------------------------------------------------------			
'''
This table is used to indicate what players can see what characters.
'''
class character_Access(models.Model):
	PID = models.ForeignKey(Player, on_delete=models.CASCADE) 
	CID = models.ForeignKey(Character, on_delete=models.CASCADE) 
	HasAccess = models.BooleanField(default = False)
	HasEdit = models.BooleanField(default = False)
	notes = models.CharField(max_length=2000,blank=True, null=True)
	class Meta:
		unique_together = (('PID', 'CID'),)
	def __str__(self):
		return self.PID.Name +' - '+ self.CID.Name
		
		
		