from django.contrib import admin
from .models import Recipe
from .models import Flavoring
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Flavoring)
