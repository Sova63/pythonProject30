from django.urls import path
from .views import *

urlpatterns = [
	path('',home,name='home'),
	path('auth/',auth,name='auth'),
	path('reg/',reg,name='reg')
]