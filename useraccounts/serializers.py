"""
Call `UserAccounts` models.
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet # , STYLE_CHOICES , LANGUAGE_CHOICES
from useraccounts.models import TblUserAccounts, TblUserDetails, TblUserPassword


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
    Create and return a new `TblUserAccounts` instance, given the validated data.
    """
    uid = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=20)
    alias_username = serializers.CharField(required=False, max_length=20)

    def create(self, validated_data):
        """
        Create and return a new `TblUserAccounts` instance, given the validated data.
        """
        return TblUserAccounts.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TblUserAccounts` instance, given the validated data.
        """
        instance.uid = validated_data.get('uid', instance.uid)
        instance.username = validated_data.get('username', instance.username)
        instance.alias_username = validated_data.get('alias_username', instance.alias_username)
        instance.save()
        return instance

class TblUserDetailsSerializer(serializers.Serializer):
    """
    Create and return a new `TblUserDetails` instance, given the validated data.
    """
    detail_id = serializers.IntegerField(read_only=True)
    useraccount = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=False, max_length=25)
    last_name = serializers.CharField(required=False, max_length=45)
    birthdate = serializers.DateTimeField(required=False)
    record_time = serializers.DateTimeField()
    creator = serializers.IntegerField(read_only=True)


    def create(self, validated_data):
        """
        Create and return a new `TblUserDetails` instance, given the validated data.
        """
        return TblUserDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TblUserDetails` instance, given the validated data.
        """
        instance.detail_id = validated_data.get('detail_id', instance.detail_id)
        instance.useraccount = validated_data.get('useraccount', instance.useraccount)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.record_time = validated_data.get('record_time', instance.record_time)
        instance.creator = validated_data.get('creator', instance.creator)

        instance.save()
        return instance

class TblUserPasswordSerializer(serializers.Serializer):
    """
    Create and return a new `useraccount` instance, given the validated data.
    """
    id_password = serializers.IntegerField(read_only=True)
    useraccount_id_pwd = serializers.IntegerField(read_only=True)
    salt = serializers.CharField(max_length=200, required=True)
    hash = serializers.CharField(max_length=200, required=True)
    record_time = serializers.DateTimeField(required=True)
    creator = serializers.IntegerField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `TblUserPassword` instance, given the validated data.
        """
        return TblUserPassword.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `TblUserPassword` instance, given the validated data.
        """
        instance.id_password = validated_data.get('id_password', instance.id_password)
        # pylint: disable=line-too-long
        instance.useraccount_id_pwd = validated_data.get('useraccount_id_pwd', instance.useraccount_id_pwd)
        instance.salt = validated_data.get('salt', instance.salt)
        instance.hash = validated_data.get('hash', instance.hash)
        instance.record_time = validated_data.get('record_time', instance.record_time)
        instance.creator = validated_data.get('creator', instance.creator)
        instance.save()
        return instance
