from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(source='user_set',read_only=True)
    class Meta:
        model = User
        fields = ('id','email','password','name','phone','token')
        extra_kwargs = {
            		"password": {"write_only": True},
                    }
    def create(self, validated_data):
        user = super(SignupSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_token(self , user):
        token = RefreshToken.for_user(user).access_token
        return str(token)