from rest_framework.mixins import (
                                    ListModelMixin, 
                                    CreateModelMixin,
                                    UpdateModelMixin, 
                                    RetrieveModelMixin,
                                    DestroyModelMixin,
                    
                                )
from rest_framework.generics import GenericAPIView

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class SnippetDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    """
    Retrieve, update or delete
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
