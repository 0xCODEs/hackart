from django.contrib import admin
from api.models import *


# Register your models here.

#class ChallengeAdmin(admin.ModelAdmin):
#  """
#  Sets the display settings for the challenge model in the django admin
#  interface.
#  """
#  list_display = ('category', 'points', 'title')

admin.site.register(Challenge)
admin.site.register(Scoreboard)
admin.site.register(Team)
admin.site.register(ChallengeTimestamp)