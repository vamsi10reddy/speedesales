from django.urls import path
from core.views import index

app_name = 'core'

urlpatterns = [
    path("urls/", index, name='index'),  # Make sure to use the view function, not a string
]
