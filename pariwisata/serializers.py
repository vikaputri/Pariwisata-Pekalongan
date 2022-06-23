from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    Article_name = serializers.ReadOnlyField(source='article.title')
    class Meta:
        model = Category
        fields = ["name", "slug", "Article_name"]

class ArticleSerializer(serializers.ModelSerializer):
    Category = CategorySerializer(many=True)
    
    class Meta:
        model = Article
        fields = ["title", "description", "content", "alamat", "telepon","jam", "harga", "slug", "image", "Category"]

class OleholehSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oleholeh
        fields = '__all__'

class KulinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kuliner
        fields = '__all__'
