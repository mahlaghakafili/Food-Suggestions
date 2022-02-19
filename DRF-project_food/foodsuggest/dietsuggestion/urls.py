from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.HomePage.as_view()),
    path('login/', views.Login.as_view()),
    path('bmi/', views.Bmi.as_view()),
    path('result/', views.Result.as_view()),
    path('info/', views.Info.as_view()),
    path('contact/', views.Contact.as_view()),
    path('lifestyle/', views.LifeStyle.as_view()),
    path('suggestion/', views.Suggestion.as_view()),
    path('logout/', views.Logout.as_view()),
    path('adminpage/', views.AdminPage.as_view()),
]
