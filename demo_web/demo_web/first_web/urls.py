from django.urls import path
from first_web import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("About/", views.about, name="About"),
    path("Registration/", views.registration, name="Registration")
]
