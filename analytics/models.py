from django.db import models

# Create your models here.
from shortener.models import conutURL


class ClickEventManager(models.Manager):
    def create_event(self, conutInstance):
        if isinstance(conutInstance, conutURL):
            obj, created = self.get_or_create(conut_url=conutInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    conut_url    = models.OneToOneField(conutURL,on_delete=models.CASCADE)
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True) 
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)