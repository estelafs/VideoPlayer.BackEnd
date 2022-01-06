from django.urls import path
from . import views

urlpatterns = [
    path('', views.history, name='history'),
    path('bookMarks/', views.bookMarks, name='bookMarks'),
    path('addEntry/', views.addEntry, name='addEntry')
]