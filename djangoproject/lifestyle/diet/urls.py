from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('bmi/', views.bmi, name="bmi"),
    path('result/', views.result, name="result"),
    path('info/', views.info, name="info"),
    path('contact/', views.contact, name="contact"),
    path('lifestyle/', views.lifestyle, name="lifestyle"),
    path('suggestion/', views.suggestion, name="suggestion"),
    path('logout/', views.logout, name="logout"),
    path('adminpage/', views.own_admin_page, name="admin_page"),
]
