from django.contrib.auth.models import User

from django.db import models
from django.template.defaultfilters import slugify


class Member(models.Model):
    member_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100,unique=True, verbose_name='member_name')
    bio = models.TextField()

    def __str__(self):
        return self.member_name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug
                 }
        return reverse('member_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.member_name)
        super(Member, self).save(*args, **kwargs)

class Team(models.Model):
    team_name = models.CharField(max_length=50, blank=False)
    members = models.ManyToManyField(Member)
    events = models.CharField(max_length=60)
    events_pub_date = models.DateTimeField('date published')

    def __str__(self):
        return (self.team_name,self.events_pub_date)

class Album(models.Model):
    album_name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=100, unique=True, verbose_name="album_name")
    members = models.ManyToManyField(Member)
    album_pub_date= models.DateTimeField('date published')

    def __str__(self):
        return self.album_name

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('album_detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug= slugify(self.album_name)
        super(Album, self).save(*args, **kwargs)
