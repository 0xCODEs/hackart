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
  correctflags = models.IntegerField(default=0)
  wrongflags = models.IntegerField(default=0)
  user = models.OneToOneField(User, related_name='teams', related_query_name='team')
  solved = models.ManyToManyField('Challenge', blank=True, related_name='solved', through='challenge_timestamp')
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


class Challenge_Timestamp(models.Model):
  """
  Challenge timestamp model class.
  """
  team = models.ForeignKey('Team', related_name='challenge_timestamps', related_query_name='challenge_timestamp')
  challenge = models.ForeignKey('Challenge', related_name='challenge_timestamps', related_query_name='challenge_timestamp')
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'Challenge_Timestamps'