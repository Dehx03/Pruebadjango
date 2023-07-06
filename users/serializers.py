from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','last_name','email')


class Registro(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'last_name','email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],last_name=validated_data['last_name'], email=validated_data['email'], password=validated_data['password'])

        return user