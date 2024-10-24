from django.urls import path
from userauths.views import registration_page

app_name = 'userauths'

urlpatterns = [
    path("sign-up/", registration_page, name='registration_page'),  # Make sure to use the view function, not a string
]
