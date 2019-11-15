"""
Call `UserAccounts` models.
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from useraccount.models import TblUserAccounts, TblUserDetails, TblUserPassword


class UserSerializer(serializers.ModelSerializer):
    """
    Class docstring
    """
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets', 'owner',]

class TblUserAccountsSerializer(serializers.Serializer):
    """
    Create and return a new `useraccount` instance, given the validated data.
    """
    uid = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    alias_username = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return TblUserAccounts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.uid = validated_data.get('uid', instance.uid)
        instance.username = validated_data.get('username', instance.username)
        instance.alias_username = validated_data.get('alias_username', instance.alias_username)
        instance.save()
        return instance

class TblUserDetailsSerializer(serializers.Serializer):
    """
    Create and return a new `useraccount` instance, given the validated data.
    """
    uid = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    alias_username = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return TblUserAccounts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.uid = validated_data.get('uid', instance.uid)
        instance.username = validated_data.get('username', instance.username)
        instance.alias_username = validated_data.get('alias_username', instance.alias_username)
        instance.save()
        return instance

class TblUserPasswordSerializer(serializers.Serializer):
    """
    Create and return a new `useraccount` instance, given the validated data.
    """
    id_password = serializers.IntegerField(read_only=True)
    useraccount_id_pwd = serializers.IntegerField(read_only=True)
    salt = serializers.IntegerField(read_only=True)
    hash = serializers.IntegerField(read_only=True)
    record_time = serializers.CharField(required=False, allow_blank=True, max_length=100)
    creator = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return TblUserAccounts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.uid = validated_data.get('uid', instance.uid)
        instance.username = validated_data.get('username', instance.username)
        instance.alias_username = validated_data.get('alias_username', instance.alias_username)
        instance.save()
        return instance