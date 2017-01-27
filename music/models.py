from __future__ import unicode_literals


from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User)

    Adhar=models.CharField(max_length=14,default = '1234-5678-9012')
    def __unicode__(self):
        return self.username
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title =  models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favourite=models.BooleanField(default=False)
    def __str__(self):
        return self.song_title

#class Doubts()

class Transport(models.Model):
    idp = models.IntegerField()
   # location = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    #genre = models.CharField(max_length=100)

    created_date = models.DateTimeField(
        default=timezone.now)
    logo = models.FileField( default = 'music/images/2-image.jpg')

    def __str__(self):
        return self.title+' - '+str(self.idp)+' - '+str(self.logo)