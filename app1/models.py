from django.db import models

# Create your models here.

class Box(models.Model):
    boxLength = models.FloatField()
    boxHeight = models.FloatField()
    boxWidth = models.FloatField()

    def __str__(self):
        return '(%g, %g, %g)' % (self.boxHeight, self.boxLength, self.boxWidth)