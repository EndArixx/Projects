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