from __future__ import unicode_literals

from django.db import models

class Challenge(models.Model):
  """
  Challenge model class.
  """
  title = models.CharField(max_length=200)
  points = models.IntegerField(default=0)
  description = models.CharField(max_length=10000)
  flag = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Challenges'

  class JSONAPIMeta:
    resource_name = "challenge"

"""
  def _get_number_solved(self):
    return self.challenge_timestamps.count()
  numsolved = property(_get_number_solved)
"""
