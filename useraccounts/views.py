"""
Rewriting our API using generic class-based views
"""

# ================================
# Using generic class-based views
# ================================

from rest_framework import permissions, generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from useraccounts.models import TblUserAccounts, TblUserDetails, TblUserPassword
from snippets.serializers import SnippetSerializer
from snippets.permissions import IsOwnerOrReadOnly

class UsersList(generics.ListCreateAPIView):
    """
    List of users
    """
    queryset = TblUserAccounts.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        """
        Create snippet list
        """
        serializer.save(owner=self.request.user)

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    user details
    """
    queryset = TblUserDetails.objects.all()
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
