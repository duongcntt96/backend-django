from django.urls import path
from . import views
app_name = "phuongtien"
urlpatterns = [
    path('', views.index, name="index"),
]
