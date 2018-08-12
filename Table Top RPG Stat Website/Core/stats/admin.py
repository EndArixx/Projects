from django.contrib import admin

#Player
from .models import  Player
from .models import  Faction
from .models import  Group
admin.site.register(Player)
admin.site.register(Faction)
admin.site.register(Group)

#Character
from .models import  Character
from .models import  Character_HP
admin.site.register(Character)
admin.site.register(Character_HP)

#Armor
from .models import  Armor
from .models import  Character_Equipped_Armor
from .models import  Character_Equipped_Armor_Value
admin.site.register(Armor)
admin.site.register(Character_Equipped_Armor)
admin.site.register(Character_Equipped_Armor_Value)

#Weapon
from .models import  Weapon_Range
from .models import  Weapon_Ammo
from .models import  Weapon
from .models import  Weapon_Character
admin.site.register(Weapon_Range)
admin.site.register(Weapon_Ammo)
admin.site.register(Weapon)
admin.site.register(Weapon_Character)

#Stat & Skill
from .models import  Stat
from .models import  Character_Stat
from .models import  Skill
from .models import  Character_Skill
from .models import  Character_Meta
admin.site.register(Stat)
admin.site.register(Character_Stat)
admin.site.register(Skill)
admin.site.register(Character_Skill)
admin.site.register(Character_Meta)

#Item
from .models import  Item
from .models import  Vehicle
from .models import  Vehicle_Upgrade
admin.site.register(Item)
admin.site.register(Vehicle)
admin.site.register(Vehicle_Upgrade)

#Status
from .models import  Status
from .models import  Character_Status
from .models import  Vehicle_Status	
admin.site.register(Status)
admin.site.register(Character_Status)
admin.site.register(Vehicle_Status)	

#NPC
from .models import NPC
from .models import NPC_Disposition
admin.site.register(NPC)
admin.site.register(NPC_Disposition)


#Misc
from .models import  War_Crime
admin.site.register(War_Crime)

#Administration
from .models import  character_Access
admin.site.register(character_Access)\