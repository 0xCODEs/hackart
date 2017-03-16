from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import time

class Team(models.Model):
  """
  Team model class.
  """
  scoreboard = models.ForeignKey('Scoreboard', related_name='teams', related_query_name='team')
  team_name = models.CharField(max_length=60, unique=True)
  points = models.IntegerField(default=0)
  correct_flags = models.IntegerField(default=0)
  wrong_flags = models.IntegerField(default=0)
  user = models.OneToOneField(User, related_name='team', related_query_name='team')
  solved = models.ManyToManyField('Challenge', blank=True, related_name='solved', through='ChallengeTimestamp')
  last_timestamp = models.DateTimeField(default=datetime.fromtimestamp(0))
  created = models.DateTimeField(auto_now_add=True)
    
  class Meta:
    verbose_name_plural = 'Teams'

  def __unicode__(self):
    return '{}'.format(self.team_name)

  def solves(self):
    challenge_timestamps = []
    team_challenge_timestamps = self.challenge_timestamps.all()
    for timestamp in team_challenge_timestamps:
      _time = int(time.mktime(timestamp.created.timetuple()))
      _id = timestamp.challenge.id
      challenge_timestamps.append((_id, _time))
    return challenge_timestamps

  def lasttimestamp(self):
    return int(self.last_timestamp.strftime('%s'))

  def team(self):
    """
    Alias for teamname.
    Created for ctftime api.
    """
    return self.team_name

  def score(self):
    """
    Alias for points.
    Created for ctftime api.
    """
    return self.points