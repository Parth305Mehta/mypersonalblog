from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from blog import views
urlpatterns = [
    url(r'^email/$',views.sendmail,name='sendmail'),
    url(r'^$',views.backpage,name='base'),
]