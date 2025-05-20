from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserHelloView.as_view(), name='user_hello'),
]