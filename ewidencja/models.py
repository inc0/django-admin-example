from django.db import models

class City(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return self.name