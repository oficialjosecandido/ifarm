from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("llogin", views.login_view, name="llogin"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]