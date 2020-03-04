from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ('id','owner','created_time','type','source_type','source_id','input_meta_data',)