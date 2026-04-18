from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('predict/', views.predict, name='predict'),

    # NEW
    path('upload/', views.upload_page, name='upload_page'),
    path('live/', views.live_page, name='live_page'),

    path('guide/', views.guide, name='guide'),
    path('emergency/', views.emergency, name='emergency'),
    path('about/', views.about, name='about'),
]