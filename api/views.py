from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserSerializerWithToken, AudioSerializer
from .models import Audio


@api_view(['GET'])
def checkToken(request):

    serializer = UserSerializer(request.user)
    print(serializer.data)
    return Response(serializer.data)


class Signup(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data, "message": "User sign up successfully", "statusCode": 200}, status=status.HTTP_200_OK, )
        return Response({"data": None, "message": serializer.errors['username'][0], "statusCode": 400}, status=status.HTTP_200_OK)


@api_view(['POST'])
def CreateAudio(request):
    serializer = AudioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data, "message": "Audio created successfully", "statusCode": 200}, status=status.HTTP_200_OK, )
    return Response({"data": None, "message": serializer.errors, "statusCode": 400}, status=status.HTTP_200_OK)


@api_view(['GET'])
def AudioList(request):
    audios = Audio.objects.all()
    serializer = AudioSerializer(audios)
    if serializer.is_valid():
        return Response({"data": serializer.data, "message": "Audio created successfully", "statusCode": 200}, status=status.HTTP_200_OK, )
