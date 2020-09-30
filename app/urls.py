from django.urls import path
from app import views

urlpatterns = [
    path("journals", views.Journals_LA.as_view()),
    path("journals/<int:id>", views.Journals_RUD.as_view()),
    path("charts-of-accounts", views.ChartsOfAccount_LA.as_view()),
    path("charts-of-accounts/<int:id>", views.ChartsOfAccount_RUD.as_view()),
    path("unit-of-measurement", views.UnitOfMeasurement_LA.as_view()),
    path("unit-of-measurement/<int:id>", views.UnitOfMeasurement_RUD.as_view()),
    ]
