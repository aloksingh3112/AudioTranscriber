from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .validation import ValidateCaps, ValidateSet, ValidationSpace, ValidateStringTerminators, ValidateStringPausers

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
            return Response({"data": serializer.data, "message": "User sign up successfully"}, status=status.HTTP_200_OK, )
        return Response({"data": None, "message": serializer.errors['username'][0]}, status=status.HTTP_403_FORBIDDEN)


# @api_view(['POST'])
# def CreateAudio(request):
#     serializer = AudioSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"data": serializer.data, "message": "Audio created successfully", "statusCode": 200}, status=status.HTTP_200_OK, )
#     return Response({"data": None, "message": serializer.errors, "statusCode": 400}, status=status.HTTP_200_OK)


@api_view(['GET'])
def AudioLists(request):
    audios = Audio.objects.all()
    serializer = AudioSerializer(audios, many=True)
    return Response({"data": serializer.data, "message": "Audio fetch successfully"}, status=status.HTTP_200_OK, )


@api_view(['GET'])
def AudioList(request, pk):
    audio = Audio.objects.get(id=pk)
    serializer = AudioSerializer(audio, many=False)
    return Response({"data": serializer.data, "message": "Audio fetch successfully", "statusCode": 200}, status=status.HTTP_200_OK, )


@api_view(['POST'])
def MapAudioUser(request):
    print(request.data['id'], request.user)
    text = request.data['transcribedData']
    if not(ValidateSet(text)):
        return Response({"data": None, "message": "Please enter valid characters"}, status=status.HTTP_400_BAD_REQUEST, )

    if not(ValidateCaps(text)):
        return Response({"data": None, "message": "Please enter either first letter of word capital or every character of word capital"}, status=status.HTTP_400_BAD_REQUEST, )

    if not(ValidationSpace(text)):
        return Response({"data": None, "message": "Please enter only one space between words"}, status=status.HTTP_400_BAD_REQUEST, )

    if not(ValidateStringTerminators(text)):
        return Response({"data": None, "message": "Please use punctuation(.?!) correctly"}, status=status.HTTP_400_BAD_REQUEST, )

    if not(ValidateStringPausers(text)):
        return Response({"data": None, "message": "Please use punctuation(,;:) correctly"}, status=status.HTTP_400_BAD_REQUEST, )

    audio = Audio.objects.get(id=request.data['id'])
    user = User.objects.get(username=request.user)
    s = UserSerializer(user)
    request.data['user'] = s.data['pk']
    serializer = AudioSerializer(instance=audio, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"data": serializer.data, "message": "Audio created successfully"}, status=status.HTTP_200_OK, )
    return Response({"data": None, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
