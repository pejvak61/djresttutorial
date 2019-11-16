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
from snippets.permissions import IsOwnerOrReadOnly
# pylint: disable=line-too-long
from useraccounts.serializers import TblUserAccountsSerializer, TblUserDetailsSerializer, TblUserPasswordSerializer



class CreateNewUser(generics.ListCreateAPIView):
    """
    Users
    """
    queryset = TblUserAccounts.objects.all()
    serializer_class = TblUserAccountsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        """
        Create new User
        """
        serializer.save(owner=self.request.user)

class ListAllUsers(generics.ListCreateAPIView):
    """
    user list
    """
    queryset = TblUserAccounts.objects.all()
    serializer_class = TblUserAccountsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CreateNewUserDetail(generics.ListCreateAPIView):
    """
    Users details
    """
    queryset = TblUserDetails.objects.all()
    serializer_class = TblUserDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        """
        Create new User
        """
        serializer.save(owner=self.request.user)

class ListAllUserDetails(generics.ListCreateAPIView):
    """
    List user details
    """
    queryset = TblUserDetails.objects.all()
    serializer_class = TblUserDetailsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CreateNewUserPassword(generics.ListCreateAPIView):
    """
    Users details
    """
    queryset = TblUserPassword.objects.all()
    serializer_class = TblUserPasswordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        """
        Create new User
        """
        serializer.save(owner=self.request.user)

class ListAllUserPasswords(generics.ListCreateAPIView):
    """
    List user details
    """
    queryset = TblUserPassword.objects.all()
    serializer_class = TblUserPasswordSerializer
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
