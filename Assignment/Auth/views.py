from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.auth.password_validation import validate_password
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import SignupSerializer





#signup view
class SignUp(APIView):
    permission_classes=(AllowAny,)
    def validate_email_address(self,email):
        try:
            validate_email(email)
            return True
        except Exception as e:
            return False

    def post(self,request,*args, **kwargs):
        data = request.data
        User = get_user_model()
        if User.objects.filter(email=data['email']).exists():
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'User with this email already exists','data':{}},
                    status=status.HTTP_400_BAD_REQUEST,
                    content_type="application/json"
                    )
        else:
            serializer = SignupSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':status.HTTP_201_CREATED,'message':'user created','data':serializer.data},
                            status=status.HTTP_201_CREATED,
                            content_type="application/json"
                            )
            else:
                return Response({'status':status.HTTP_200_OK,'message':serializer.errors,'data':{}},
                             status=status.HTTP_200_OK,
                             content_type="application/json"
                             )

#login view
class LogIn(APIView):
    permission_classes=(AllowAny,)
    def post(self, request):
        try:
            data = request.data
            User = get_user_model()
            user = User.objects.get(email=data['email'])
            print(user)
            print(user.check_password(data['password']))
            if user.check_password(data['password']) and user.is_active:
                access = RefreshToken.for_user(user).access_token
                return Response({'status':status.HTTP_200_OK,'message':'Login successful','data':{'user_id':user.id,
                'email':user.email,'name':user.name,'token':str(access)}},
                status=status.HTTP_200_OK,content_type="application/json")
            else:
                return Response({'status':status.HTTP_401_UNAUTHORIZED,'message':'Invalid credentials or inactive user','data':{}},
                status=status.HTTP_401_UNAUTHORIZED,content_type="application/json")
        except Exception as e:
            return Response({'status':status.HTTP_401_UNAUTHORIZED,'message':'Invalid email or password address','data':{}},
            status=status.HTTP_401_UNAUTHORIZED,content_type="application/json")