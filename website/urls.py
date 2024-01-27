from django.urls import path, include
import website.views as views
urlpatterns = [
    path("", views.index, name="index"),
]
