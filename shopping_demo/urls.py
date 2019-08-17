from django.urls import re_path
from . import views

urlpatterns=[
    re_path('^$', views.e_shop_test, name='eshop-test'),
]

