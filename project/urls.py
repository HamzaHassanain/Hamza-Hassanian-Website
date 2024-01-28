
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("website.urls")),
    path('favicon.ico', lambda _ : redirect('/static/Icon.png', permanent=True)),

]
