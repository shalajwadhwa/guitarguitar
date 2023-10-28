from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("orders/", views.orders, name="orders"),
    path("chat/", views.chat, name="chat"),
    path("answer/", views.answer.as_view(), name="answer"),]