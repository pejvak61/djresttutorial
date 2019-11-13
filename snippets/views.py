"""
Rewriting our API using class-based views
"""

# ================================
# Using generic class-based views
# ================================

from rest_framework import permissions, generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly



class SnippetList(generics.ListCreateAPIView):
    """
    List of snippets
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        """
        Create snippet list
        """
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    snippet details
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    """
    List of Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    User details
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
