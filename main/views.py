from django.shortcuts import render
from django.views.generic import TemplateView

class Welcome(TemplateView):
	template_name = 'main/home.html'