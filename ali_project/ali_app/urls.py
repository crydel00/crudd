from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name='home_page'),
    path('news/all/',views.news_page, name='news_page'),
    path('news/detail/<int:pk>',views.details_page, name='details_page')
]