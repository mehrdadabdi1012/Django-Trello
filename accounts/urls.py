from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
   path('', views.AccountView.as_view() , name='account'),
]
