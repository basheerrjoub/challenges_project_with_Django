from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),#challenges/
    path('<int:day>', views.weekly_challenges_number),
    path("<str:day>", views.weekly_challenges, name="weekly-challenge")
    
]
