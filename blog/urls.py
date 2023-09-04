from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('hello/', say_hello, name='hello'),
    path('category/<slug:cat>/', category, name='category'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]

