from django.urls import path;

from . import views;

#URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('hello-02/', views.say_hello_2)
];