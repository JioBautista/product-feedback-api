from django.shortcuts import render
from rest_framework import generics
from api.models import CurrentUser
from api.serializers import CurrentUserSerializer


class CurrentUserList(generics.ListCreateAPIView):
    queryset = CurrentUser.objects.all()
    serializer_class = CurrentUserSerializer


class CurrentUserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = CurrentUser.objects.all()
    serializer_class = CurrentUserSerializer
