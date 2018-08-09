from django.contrib import admin
from .models import Player
from .models import Group
from .models import Character
from .models import Character_HP
from .models import War_Crime
from .models import character_Access
from .models import Armor
from .models import Character_Equipped_Armor
from .models import Character_Equipped_Armor_Value
from .models import Item

# Register your models here.
admin.site.register(Player)
admin.site.register(Group)
admin.site.register(Character)
admin.site.register(Character_HP)
admin.site.register(War_Crime)
admin.site.register(character_Access)
admin.site.register(Armor)
admin.site.register(Character_Equipped_Armor)
admin.site.register(Character_Equipped_Armor_Value)
admin.site.register(Item)