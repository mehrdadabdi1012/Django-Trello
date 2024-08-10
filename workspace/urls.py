from django.urls import path, include
from . import views

app_name = 'workspace'
urlpatterns = [
   path('', views.HomeView.as_view() , name='workspace'),
]
