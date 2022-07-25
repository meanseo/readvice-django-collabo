from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response

from books import api
from books.models import Book
from books.serializers import BookSerializer

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
    # 정보나루 API 및 데이터 정제
    SUBSCRIPTION_KEY = configs.data_book_api_key
    # url2 = f'http://data4library.kr/api/libSrchByBook?authKey={config.data_book_api_key}&isbn=[ISBN]&region=[지역코드]'
    url = f'http://data4library.kr/api/loanItemSrch?authKey={configs.data_book_api_key}&startDt=2022-07-10&endDt=2022-07-12&format=json'
    # queryParams = '&' + urlencode({quote_plus('page'): '1', quote_plus('perPage'): '1824', quote_plus('returnType'): 'JSON'})

    response = urllib.request.urlopen(url).read()
    # json_str = response.read().decode("utf-8")
    json_object = json.loads(response)
    # body = json_object['response']
    # json_object = body['docs']
    # del json_object['doc']
    # ic(json_object)

    book_list = [json_object[i]['doc'] for i in range(0, len(json_object))]
    # ic(book_list)

    df = pd.DataFrame.from_records(book_list)
    # ic(df)

    df.drop(['addition_symbol', 'class_no', 'loan_count', 'no', 'publication_year', 'ranking', 'vol', 'publisher'],
            axis=1, inplace=True)
    df.columns = ['book_title', 'authors', 'isbn', 'category', 'book_img']
    df2json = df.to_json(orient="index")
    df2json = json.loads(df2json)
    book_api_data = df2json.values()
    ic(book_api_data)
    return Response(book_api_data)

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


