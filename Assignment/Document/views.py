from .models import Document
from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import Http404
from .serializers import DocumentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import IntegrityError


class DocumentView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        data = Document.objects.filter(id=request.GET.get('id'))
        if data:
            serializer = DocumentSerializer(data, many = True)
            return Response({'status':status.HTTP_200_OK,'data':serializer.data},
                            status=status.HTTP_200_OK,
                            content_type="application/json"
                            )
        else:
            return Response({'status':status.HTTP_200_OK,'message':'not Found','data':[]},
                            status=status.HTTP_200_OK,
                            content_type="application/json")


    def post(self, request, format=None):
        try:
            serializer = DocumentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':status.HTTP_201_CREATED,'message':'Document created','data':serializer.data},
                            status=status.HTTP_201_CREATED,
                            content_type="application/json")
            else:
                return Response({'status':status.HTTP_400_BAD_REQUEST,'message':serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST,
                                content_type="application/json")
        except Exception as e:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'empty data or incorrect fields'},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json")



    def delete(self, request, format=None):
        try:
            Document.objects.filter(id=request.GET.get('id')).delete()
            return Response({'status':status.HTTP_200_OK,'message':'Document Deleted'},
                                status=status.HTTP_200_OK,
                                content_type="application/json")

        except Exception as e:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':"Exception","data":{}},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json")

    def put(self, request, format=None):
        try:
            Document.objects.filter(id=request.GET.get('id')).update(**request.data)
            return Response({'status':status.HTTP_200_OK,'message':'Document Updated'},
                                status=status.HTTP_200_OK,
                                content_type="application/json")
        except IntegrityError:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':"invalid id in the data"},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json"
                            )
        except Exception as e:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':"Exception","data":{}},
                            status=status.HTTP_400_BAD_REQUEST,
                            content_type="application/json")


class DocumentListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        data = Document.objects.filter(owner=request.user.id)
        if data:
            paginator = Paginator(data,request.GET.get('items_per_page'))
            page = request.GET.get('page',request.GET.get('page_no'))
            document = paginator.get_page(page)
            serializer = DocumentSerializer(document, many = True)
            page_num = int(request.GET.get('page_no'))
            if (page_num<=0)or(page_num>paginator.num_pages):
                return Response({'status':status.HTTP_204_NO_CONTENT,'message':'Empty Records','data':{}},
                                status=status.HTTP_204_NO_CONTENT,
                                content_type="application/json"
                                )
            else:
                return Response({'status':status.HTTP_200_OK,'message':'Found','data':{"Document_data":serializer.data}},
                                status=status.HTTP_200_OK,
                                content_type="application/json"
                                )
        else:
            return Response({'status':status.HTTP_200_OK,'message':'not Found','data':[]},
                            status=status.HTTP_200_OK,
                            content_type="application/json")