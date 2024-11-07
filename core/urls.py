from django.urls import path
from core.views import index, indexOld, tech, techProduct
from .views import LandingPageView  

app_name = 'core'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),  # Landing page view
    path("urls/", index, name='index'),  # Make sure to use the view function, not a string
    path("old/", indexOld, name='indexOld'),
    path("tech/", tech, name="tech"),
    path('api/tech-products/', techProduct, name='tech_product_list')
]
