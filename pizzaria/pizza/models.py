from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    ingredients = models.TextField()

    def __unicode__(self):
        return u'Pizza: {}'.format(self.name)

    def __repr__(self):
        return unicode(self)
