from django.shortcuts import render 
from django.views.generic import TemplateView

# Create your views here.
class HomepageView (TemplateView):
    template_name = 'home.html'

class AboutepageView(TemplateView):
    template_name= 'about.html'
