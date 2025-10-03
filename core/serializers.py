from djoser.serializers import UserCreateSerializer as Base, UserSerializer as Base02

from rest_framework import serializers

class UserCreateSerializer(Base):

    class Meta(Base.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

class UserSerializer(Base02):
    class Meta(Base02.Meta):
        fields = ['id', 'first_name', 'email', 'last_name', 'username']