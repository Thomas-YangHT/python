from django.conf.urls import include, url

from . import view
from . import student
 
urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^student/chengji$', student.chengji_form),
    url(r'^student/query$', student.query),
    url(r'^student/', student.home),
]
