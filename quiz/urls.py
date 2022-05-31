from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("quiz",views.quiz,name="quiz"),
    path("result",views.getPredictions,name="result")
]
