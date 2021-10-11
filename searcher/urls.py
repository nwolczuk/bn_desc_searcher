from django.urls import path

from . import views

app_name = 'searcher'

urlpatterns=[
    path('home/', views.home, name='home')
]