from django.urls import path, include
import website.views as views
urlpatterns = [
    path("", views.index, name="index"),
    path("projects/<slug:slug>", views.single_project, name="project"),
]
