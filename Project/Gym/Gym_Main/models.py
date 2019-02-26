from django.db import models

# Create your models here.


class Music(models.Model):
	name_music=models.CharField(max_length=200)
	time=models.CharField(max_length=50)
	type_Music=models.CharField(max_length=80)

	def __str__(self):
		return '%s %s' %(self.name ,self.type_Music)


class Musician(models.Model):
	first_name=models.CharField(max_length=70)
	last_name=models.CharField(max_length=70)
	instrument=models.CharField(max_length=80)
	musics=models.ManyToManyField(Music)
	def __str__(self):
       return '%s %s' %(self.first_name ,self.last_name)
