from django.conf.urls import url
from . import views

urlpatterns=[
	url('index',views.index, name='index'),
	url('results.html',views.receiver, name='receiver'),
	url('main',views.main, name='main'),
	url('test',views.test, name='test'),
]
