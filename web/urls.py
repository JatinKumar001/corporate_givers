from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="web"),
    path("event/", views.event, name="eventpage"),
    path("eventpost/", views.eventpost, name="eventpage"),
    path("contact/", views.contact, name="contact"),
    path("service/", views.service, name="service"),
    path("sign/", views.sign, name="sign"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
]