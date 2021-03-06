from django.contrib.auth.models import User
from rest_framework import permissions

from rest_framework.generics import (
                                    ListCreateAPIView, 
                                    RetrieveUpdateDestroyAPIView,
                                    ListAPIView,
                                    RetrieveAPIView,
                                    )
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly



class SnippetList(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # add user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly,]

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    