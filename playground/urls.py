from django.urls import path;

from . import views;

#URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('hello-02/', views.say_hello_2),
    path('hello-03/', views.say_hello_3),
    path('hello-04/', views.say_hello_4),
    path('hello-05/', views.say_hello_5),
    path('hello-06/', views.say_hello_6),
    path('hello-07/', views.say_hello_7),
];