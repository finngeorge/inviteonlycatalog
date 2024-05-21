import uuid
from django.db import models


class User(models.Model):
  id = models.AutoField(primary_key=True)
  email = models.CharField(max_length=100, unique=True)
  password = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Artist(models.Model):
  artist_name = models.CharField(blank=True, max_length=100)
  created_by = models.ForeignKey('User', on_delete=models.CASCADE)


class Genre(models.Model):
  genre_name = models.CharField(blank=True, max_length=100)


class MiscTag(models.Model):
  tag_name = models.CharField(blank=True, max_length=100)


class Producer(models.Model):
  producer_name = models.CharField(max_length=100)


class Engineer(models.Model):
  engineer_name = models.CharField(max_length=100)


class Writer(models.Model):
  writer_name = models.CharField(max_length=100)


# Future Development: Versioning? e.g. version = models.AutoField()
class Track(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=100)
  artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
  bpm = models.DecimalField(max_digits=3, decimal_places=2)
  genres = models.ManyToManyField(Genre)
  misc_tags = models.ManyToManyField(MiscTag)
  audio_file = models.FileField() # add some more later
  uploaded_by = models.ForeignKey('User', on_delete=models.CASCADE)
  uploaded_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  producer = models.ManyToManyField(Producer)
  engineer = models.ManyToManyField(Engineer)
  writer = models.ManyToManyField(Writer)


class Collection(models.Model):
  collection_name = models.CharField(max_length=100)
  track = models.ManyToManyField(Track)
  tag = models.ForeignKey('MiscTag', on_delete=models.CASCADE)
  image = models.ImageField() # add some more later
  owner = models.ForeignKey('User', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)