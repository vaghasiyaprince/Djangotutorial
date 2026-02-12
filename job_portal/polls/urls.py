from django.urls import path

from . import views

urlpatterns = [
    path("polls/", views.index, name="index"),
    path('add',views.add,name='add'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("", views.home, name="home"),
    path("logout", views.logout_request, name="logout"),
]