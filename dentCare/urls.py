"""dentCare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from about.views import about
from appointment.views import appointment
from contact.views import contact
from service.views import service
from team.views import team
from testimonial.views import testimonial
from price.views import price
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about,name="about"),
    path('app/', appointment,name="app"),
    path('contact/', contact,name="contact"),
    path('ser/', service,name="service"),
    path('team/', team,name="team"),
    path('test/', testimonial,name="test"),
    path('home/', home,name="home"),
    path('price/', price,name="price"),
]
