from django.urls import path
from . import views

urlpatterns = [
                path('', views.feed, name = "feed"),
                path('novelty/<int:pk>/', views.novelty_detail, name = "novelty_detail"),
                ]
