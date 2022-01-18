from django.urls import path
from .views import SignUpView, LoadUserView

urlpatterns = [
    path("signup", SignUpView.as_view()),
    path("user", LoadUserView.as_view()),
]
