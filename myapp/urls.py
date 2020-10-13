from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name="main"),
    path('news/', views.mainviews.as_view()),
    path('news/<int:p_sid>/', views.abuot, name="about"),
    path('news/create/', views.create.as_view())


]