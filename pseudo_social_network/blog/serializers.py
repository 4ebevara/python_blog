from rest_framework import serializers
from .models import Category, Publication
from rest_framework.serializers import ModelSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class PublicationSerializer(ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'
        read_only_fields = ('author',)
