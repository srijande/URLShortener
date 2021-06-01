from django.db import models
from django.utils import timezone

# Create your models here.
import random 
from string import ascii_letters

class Shortener(models.Model):

    original_link = models.URLField(max_length = 500)
    shortened_link = models.CharField(max_length = 20,default=None,blank=True,null=True, unique=True)
    clicks = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now, blank=True)
       

    def random_link(self):
        random_links = ''.join(random.sample(ascii_letters,6))
        while True:
            try:
                if Shortener.objects.get(shortened_link=random_links):
                    random_links = ''.join(random.sample(ascii_letters,6))
                else:
                    break 
            except:
                return random_links

    def save(self, *args, **kwargs):
        if not self.shortened_link:
            self.shortened_link = self.random_link()
        super(Shortener, self).save(*args, **kwargs) 

    def __str__(self):
        return self.original_link

    def get_short_url(self):
        shortened_link = self.shortened_link
        url_path = 'http://127.0.0.1:8000/' + shortened_link
        return url_path
