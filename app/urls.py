from django.urls import path
from app import views

urlpatterns = [
    path("journals", views.Journals_LA.as_view()),
    path("journals", views.Journals_RUD.as_view()),
    ]
