from django.urls import path
from . import views

urlpatterns = [
                path('', views.feed, name = "feed"),
                path('novelty/<int:pk>/', views.novelty_detail, name = "novelty_detail"),
                path('novelty/new/', views.novelty_new, name="novelty_new"),
                path('novelty/edit/<int:pk>/', views.novelty_edit, name="novelty_edit"),
                ]
