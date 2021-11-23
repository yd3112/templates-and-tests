from os import name
from django.urls import path
from .views import AboutepageView, HomepageView

urlpatterns = [
   path('', HomepageView.as_view(), name='home'),
   path('about/', AboutepageView.as_view(), name='about'), 
]
