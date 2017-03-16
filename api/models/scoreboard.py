from __future__ import unicode_literals
from django.db import models

class Scoreboard(models.Model):
  """
  Scoreboard model class.
  """
  numtopteams = models.IntegerField(default=10)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Scoreboards'

  class JSONAPIMeta:
    resource_name = "scoreboard"

  def __unicode__(self):
    return '{}'.format(self.id)