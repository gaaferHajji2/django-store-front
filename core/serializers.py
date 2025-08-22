from djoser.serializers import UserCreateSerializer as Base

from rest_framework import serializers

class UserCreateSerializer(Base):

    class Meta(Base.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']