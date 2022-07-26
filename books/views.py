from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response

import books.api
import configs
from books import api
from books.models import Book
from books.serializers import BookSerializer, ApiSerializer

import json
from icecream import ic
import configs
import urllib.request
import pandas as pd

@api_view(["GET"])
@parser_classes([JSONParser])
def search(request):
    print("1.books로 들어옴")
    try:
        if request.method == 'GET':
            print("2. GET 들어옴")
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)
    except:
        return JsonResponse({'books': 'fail'})

@api_view(["POST"])
@parser_classes([JSONParser])
def add_test(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('3. 들어온 내부값: ', serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print('error: ', serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@parser_classes([JSONParser])
def book_api_data(request):
    data = books.api.book_process(request)
    # serializer = ApiSerializer(data)
    # return Response(serializer.data)
    return data

@api_view(["GET"])
@parser_classes([JSONParser])
def book_api_data2(request):
    with open('./data/isbn_books.json', 'r') as file:
        data = json.load(file)
    # ic(data)

    data = sum(data, [])
    # ic(data)

    book_list = [data[i]['book'] for i in range(0, len(data))]
    # ic(book_list)

    df = pd.DataFrame.from_records(book_list)
    # ic(df)

    df.drop(['no', 'publication_date', 'class_no', 'publisher', 'publication_year', 'isbn'], axis=1, inplace=True)
    pd.columns = ['book_title', 'author', 'category', 'book_img', 'isbn', 'book_info']
    df2json = df.to_json(orient="index")
    df2json = json.loads(df2json)
    book_api_data = df2json.values()
    return book_api_data


