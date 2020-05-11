from django.urls import path
from .views import checkToken, Signup, AudioList, MapAudioUser, AudioLists
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('check-token/', checkToken),
    path('login/', obtain_jwt_token),
    path('signup/', Signup.as_view()),
    path('getAudio/', AudioLists),
    path('getAudio/<str:pk>/', AudioList),

    path('addTranscribe/', MapAudioUser),

]
