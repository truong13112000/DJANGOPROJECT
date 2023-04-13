from django.urls import path

from . import views
urlpatterns = [
    path('product/', views.get_home, name="get_home"),
   
]