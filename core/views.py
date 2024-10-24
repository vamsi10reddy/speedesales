from django.http import HttpResponse  
from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    def get(self, request):
        return render(request, 'landingpage/landing.html')

def index(request):
    return render(request, 'core/index.html') 
