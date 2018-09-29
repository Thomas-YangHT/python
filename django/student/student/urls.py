from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url
from . import view
 
urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^student/chengji$', student.chengji_form),
    url(r'^student/query$', student.query),
    url(r'^student/', student.home),

]
