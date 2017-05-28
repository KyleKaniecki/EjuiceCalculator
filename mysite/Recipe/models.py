from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=20)
    targetAmount = models.PositiveIntegerField()
    targetNicotine = models.DecimalField(max_digits=2,decimal_places=1)
    vgRatio = models.PositiveIntegerField()
    pgRatio = models.PositiveIntegerField()
    daysToSteep = models.PositiveIntegerField()
    notes = models.TextField(default="")

    def __str__(self):
        return self.name


class Flavoring(models.Model):
    name = models.CharField(max_length=15)
    percentage = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=15)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
