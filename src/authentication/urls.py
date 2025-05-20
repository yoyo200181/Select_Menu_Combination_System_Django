from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserHelloView.as_view(), name='user_hello'),
    path('signup/', views.UserCreateView.as_view(), name='sign_up'),
]