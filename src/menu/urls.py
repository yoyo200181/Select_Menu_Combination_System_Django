from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuHelloView.as_view(), name='user_hello'),
]
