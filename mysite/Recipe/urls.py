from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.recipe_list, name='recipe_list'),
]