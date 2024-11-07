from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Product

class LandingPageView(View):
    def get(self, request):
        return render(request, 'landingpage/landing.html')

def index(request):
    return render(request, 'core/index.html') 

def tech(request):
    return render(request, 'core/tech.html') 


def indexOld(request):
    return render(request, 'core/indexOld.html') 

def techProduct(request):
    techProduct = Product.objects.values('name','description','price')
    return JsonResponse(list(techProduct), safe=False)