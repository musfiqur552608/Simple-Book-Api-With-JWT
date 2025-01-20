from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    published_date = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = Book
        fields = "__all__"