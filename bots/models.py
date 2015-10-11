from django.db import models

class Author(models.Model):
    username = models.CharField(max_length = 20)
    Name = models.CharField(max_length = 100)
    Contact = models.BigIntegerField()
    Email = models.EmailField()
    password = models.CharField(max_length = 100)
    attempts = models.IntegerField()
    def __unicode__(self):
        return self.Name

class Bot(models.Model):
    author = models.ForeignKey(Author)
    Name = models.CharField(max_length = 100)
    rec_datetime = models.DateTimeField('date recieved')
    code = models.FileField(upload_to = 'bots')
    wins = models.IntegerField()    
    loss = models.IntegerField()
    draw = models.IntegerField() #disqualifications
    ldrbrd_pos = models.IntegerField(null = True, blank = True)
    def __unicode__(self):
        return self.Name

class Log(models.Model):
    bot1 = models.ForeignKey(Bot, related_name = 'bot1')
    bot2 = models.ForeignKey(Bot, related_name = 'bot2')
    winner = models.ForeignKey(Bot, related_name = 'winner', null = True, blank = True)
    loser = models.ForeignKey(Bot, related_name = 'loser', null = True, blank = True)
    logfile = models.FileField(upload_to = 'logfiles')
    #logdata = models.TextField()
    def __unicode__(self):
        return ':'.join((self.bot1.Name, 'vs', self.bot2.Name)) 
