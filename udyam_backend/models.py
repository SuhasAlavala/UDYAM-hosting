from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Event(models.Model):
    eventnames = [
        ('SL', 'Select Event'),
        ('Mosaic', 'Mosaic'),
        ('Spybits', 'Spybits'),
        ('Digisim', 'Digisim'),
        ('Continuum', 'Continuum'),
        ('Cassandra', 'Cassandra'),
        ('Commnet', 'Commnet'),
        ('Funckit', 'Funckit'),
        ('X-IoT-A', 'X-IoT-A'),
        ('I-Chip', 'I-Chip')
    ]

    eventname = models.CharField(max_length=20, choices=eventnames, default='SL')
    members_from_1st_year = models.IntegerField()
    members_after_1st_year = models.IntegerField()
    score = models.IntegerField(blank=True)

    def __str__(self):
        return self.eventname

class Team(models.Model):
    members = [
        ('SL', 'Select No. of Members'),
        ('1', '1'),
        ('2', '2'),
        ('3,', '3')
    ]

    number_of_members = models.CharField(max_length=2, choices=members, default='SL')
    team_name = models.CharField(max_length=50)
    Team_leader = models.EmailField(max_length= 254, blank=True)
    member1 = models.EmailField(max_length= 254, blank=True)
    member2 = models.EmailField(max_length= 254, blank=True)
    member3 = models.EmailField(max_length= 254, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team_score = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.team_name

class Workshop(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    url = models.URLField(max_length=200)

    def __str__(self):
        string = str(self.event) + ', ' + str(self.date)
        return string

class Content(models.Model):
    date = models.DateField()
    context = models.CharField(max_length=500)

    def __str__(self):
        string = 'Future Context, ' + str(self.date)
        return string