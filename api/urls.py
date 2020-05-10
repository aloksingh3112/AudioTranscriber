from django.urls import path
from .views import checkToken, Signup
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('check-token/', checkToken),
    path('login/', obtain_jwt_token),
    path('signup/', Signup.as_view())
]
