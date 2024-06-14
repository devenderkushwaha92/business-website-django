from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    # path('',views.home),
    path('about/',views.about, name="about"),
    path('',views.get_name, name="home"),
    path('contact/',views.contact, name="contact"),
]
