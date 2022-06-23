from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404

class CategoryView(APIView):
	def post(self, request, *args, **kwargs):
		file_serializer = CategorySerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, slug=None):
		if slug:
			file = get_object_or_404(Category, slug=slug)
			serializer = CategorySerializer(file)
			return Response(serializer.data, status=status.HTTP_200_OK)

		files = Category.objects.all()
		if files.exists():
			serializer = CategorySerializer(files, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({"detail":"Data tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, slug=None):
		item = get_object_or_404(Category, slug=slug)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})

class ArticleView(APIView):
	def post(self, request, *args, **kwargs):
		file_serializer = ArticleSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, slug=None):
		if slug:
			file = get_object_or_404(Article, slug=slug)
			serializer = ArticleSerializer(file)
			return Response(serializer.data, status=status.HTTP_200_OK)

		files = Article.objects.all()
		if files.exists():
			serializer = ArticleSerializer(files, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({"detail":"Data tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, slug=None):
		item = get_object_or_404(Article, slug=slug)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})

class OleholehView(APIView):
	def post(self, request, *args, **kwargs):
		file_serializer = OleholehSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, slug=None):
		if slug:
			file = get_object_or_404(Oleholeh, slug=slug)
			serializer = OleholehSerializer(file)
			return Response(serializer.data, status=status.HTTP_200_OK)

		files = Oleholeh.objects.all()
		if files.exists():
			serializer = OleholehSerializer(files, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({"detail":"Data tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, slug=None):
		item = get_object_or_404(Oleholeh, slug=slug)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})

class KulinerView(APIView):
	def post(self, request, *args, **kwargs):
		file_serializer = KulinerSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, slug=None):
		if slug:
			file = get_object_or_404(Kuliner, slug=slug)
			serializer = KulinerSerializer(file)
			return Response(serializer.data, status=status.HTTP_200_OK)

		files = Kuliner.objects.all()
		if files.exists():
			serializer = KulinerSerializer(files, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response({"detail":"Data tidak ditemukan."}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, slug=None):
		item = get_object_or_404(Kuliner, slug=slug)
		item.delete()
		return Response({"status": "Berhasil", "data": "Item telah dihapus"})