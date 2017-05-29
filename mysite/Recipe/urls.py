from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.recipe_list, name='recipe_list'),
    url(r'^new/$', views.recipe_new,  name='recipe_new'),
    url(r'^recipe/(?P<pk>\d+)/$', views.recipe_edit, name='recipe_edit'),
]