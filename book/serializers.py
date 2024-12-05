from rest_framework import serializers
from .models import Book, Student, StudentBook
from django.db import models

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    published_date = serializers.DateField()
    isbn = serializers.IntegerField()
    class Meta:
        model=Book
        fields='__all__'
    def create(self, validated_data):
        return Book.objects.create(**validated_data)

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    grade = serializers.IntegerField()
    
    class Meta:
        model=Student
        fields='__all__'

class StudentBookSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    date_in = serializers.DateField()
    
    class Meta:
        model=StudentBook
        fields='__all__'