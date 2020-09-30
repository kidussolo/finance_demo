from django.urls import path
from app import views

urlpatterns = [
    path("journals", views.Journals_LA.as_view()),
    path("journals/<int:id>", views.Journals_RUD.as_view()),
    path("charts-of-accounts", views.ChartsOfAccount_LA.as_view()),
    path("charts-of-accounts/<int:id>", views.ChartsOfAccount_RUD.as_view()),
    path("unit-of-measurements", views.UnitOfMeasurement_LA.as_view()),
    path("unit-of-measurements/<int:id>", views.UnitOfMeasurement_RUD.as_view()),
    path("item-locations", views.InvItemLocation_LA.as_view()),
    path("item-locations/<int:id>", views.InvItemLocation_RUD.as_view()),
    ]
