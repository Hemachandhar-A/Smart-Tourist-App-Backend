from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('send_alert/', views.send_alert, name='send_alert'),
    path('get_alerts/', views.get_alerts, name='get_alerts'),
    path('login/', views.login_user, name='login_user'),
    path('tourists/', views.get_tourists, name='get_tourists'),


]