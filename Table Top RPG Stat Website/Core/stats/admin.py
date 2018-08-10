from django.contrib import admin
from .models import Player
from .models import Group
from .models import Character
from .models import Character_HP
from .models import War_Crime
from .models import character_Access


# Register your models here.
admin.site.register(Player)
admin.site.register(Group)
admin.site.register(Character)
admin.site.register(Character_HP)
admin.site.register(War_Crime)
admin.site.register(character_Access)


#--Armour Zone--
from .models import Armor
from .models import Character_Equipped_Armor
from .models import Character_Equipped_Armor_Value
admin.site.register(Armor)
admin.site.register(Character_Equipped_Armor)
admin.site.register(Character_Equipped_Armor_Value)


#--Skill Zone--
from .models import Skill
from .models import Character_Skill
admin.site.register(Skill)
admin.site.register(Character_Skill)
from .models import Stat
from .models import Character_Stat
admin.site.register(Stat)
admin.site.register(Character_Stat)

#--item Zone--
from .models import Item
admin.site.register(Item)