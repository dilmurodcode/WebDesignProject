from django.urls import path
from . import views


urlpatterns = [
    path('portfolio-list/', views.PortfolioAPIView.as_view()),
    path('portfolio-detail/<int:pk>/', views.PortfolioProjectProgressMixedAPIView.as_view()),

]