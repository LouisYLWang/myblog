from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'lottery', views.index, name='index'),
]