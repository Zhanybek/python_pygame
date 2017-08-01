from django.db import models

#from datetime import timezone
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class  Tournaments(models.Model):
#    [tid] INT(16) NOT NULL DEFAULT 0,
    tid = models.IntegerField(16)
#    [live] INT(8),
    live = models.IntegerField(8)
#    [name] CHAR(512),
    name = models.CharField(max_length=512)
#    [name_sh] CHAR(512),
    name_sh = models.CharField(max_length=512)
#    [city] CHAR(64),
    city = models.CharField(max_length=64)
#    [qualification] INT(8),
    qualification = models.IntegerField
#    [gender] CHAR(16),
    gender = models.CharField(max_length=16)
#    [type] CHAR(16),
    type = models.CharField(max_length=16)
#    [kind _sport] CHAR(32),
    kind_sport = models.CharField(max_length=32)
#    [sets] INT(8),
    sets = models.IntegerField
#    [prize_amount] CHAR(64),
    prize_amount = models.CharField(max_length=64)
    prize_currency = models.CharField(max_length=32)
#    [itfid] CHAR(64),
    itfid = models.CharField(max_length=64)
#    [itfname] CHAR(64),
    itfname = models.CharField(max_length=64)
#    [ground_id] CHAR(8),
    ground_id = models.CharField(max_length=8)
#    [ground_name] CHAR(32),
    ground_name = models.CharField(max_length=32)
#    [ground_mainid] CHAR(8),
    ground_mainid = models.CharField(max_length=8)
#    [ground_main] CHAR(8));
    ground_main = models.CharField(max_length=8)

    db_table = 'Tournaments'

def __str__(self):
    return self.title

class  tennisinfo(models.Model):
    gjson = models.TextField()

    db_table = 'tennisinfo'
def publish(self):
    self.published_date = timezone.now()
    self.save()