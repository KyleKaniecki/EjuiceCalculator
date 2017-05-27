from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.TextField()
    percentage = models.PositiveIntegerField()
    targetAmount = models.PositiveIntegerField()
    targetNicotine = models.PositiveIntegerField()
    vgRatio = models.PositiveIntegerField()
    pgRatio = models.PositiveIntegerField()
    daysToSteep = models.PositiveIntegerField()

    def __str__(self):
        return "%s" % (self.name)

class Flavoring(models.Model):
    name = models.CharField(max_length=30)
    percentage = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=30)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE())

    def __str__(self):
        return "%s" % (self.name)