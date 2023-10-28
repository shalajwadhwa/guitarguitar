from django.contrib import admin
from django.urls import include, path
from team20 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat/", views.chat, name='chat'),
    path("team20/", include("team20.urls")),
    path("admin/", admin.site.urls),
]
