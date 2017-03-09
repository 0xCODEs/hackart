from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import time

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

  def delete(self, *args, **kwargs):
    # get teams before deletion
    solved = self.solved.all()
    for team in solved:
      team.points -= self.points

    super(Challenge, self).delete(*args, **kwargs)

    # update teams after deletion
    for team in solved:
      team.save()

  def save(self, *args, **kwargs):
    # get solved teams
    solved = None
    if self.id:
      solved = self.solved.all()

    super(Challenge, self).save(*args, **kwargs)

    # update solved teams after changes
    if solved:
      for team in solved:
        team.save()

  def _get_number_solved(self):
    """
    Returns number of solved challenges.
    """
    return self.challenge_timestamps.count()

  numsolved = property(_get_number_solved)


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

class Team(models.Model):
  """
  Team model class.
  """
  scoreboard = models.ForeignKey('Scoreboard', related_name='teams', related_query_name='team')
  team_name = models.CharField(max_length=60, unique=True)
  points = models.IntegerField(default=0)
  correct_flags = models.IntegerField(default=0)
  wrong_flags = models.IntegerField(default=0)
  user = models.OneToOneField(User, related_name='teams', related_query_name='team')
  solved = models.ManyToManyField('Challenge', blank=True, related_name='solved', through='ChallengeTimestamp')
  last_timestamp = models.DateTimeField(default=datetime.fromtimestamp(0))
  created = models.DateTimeField(auto_now_add=True)
    
  class Meta:
    verbose_name_plural = 'Teams'

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
    return self.teamname

  def score(self):
    """
    Alias for points.
    Created for ctftime api.
    """
    return self.points


class ChallengeTimestamp(models.Model):
  """
  Challenge Timestamp model class.
  """
  team = models.ForeignKey('team', on_delete=models.CASCADE, related_name='challenge_timestamps', related_query_name='challenge_timestamp')
  challenge = models.ForeignKey('challenge', on_delete=models.CASCADE, related_name='challenge_timestamps', related_query_name='challenge_timestamp')
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'ChallengeTimestamps'
