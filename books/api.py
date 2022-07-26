import json
from icecream import ic
import configs
import urllib.request
import pandas as pd
import requests

def book_process(request):
    # 정보나루 API 및 데이터 정제
    SUBSCRIPTION_KEY = configs.data_book_api_key
    # url2 = f'http://data4library.kr/api/libSrchByBook?authKey={config.data_book_api_key}&isbn=[ISBN]&region=[지역코드]'
    url = f'http://data4library.kr/api/loanItemSrch?authKey={configs.data_book_api_key}&startDt=2022-07-10&endDt=2022-07-12&format=json'
    # queryParams = '&' + urlencode({quote_plus('page'): '1', quote_plus('perPage'): '1824', quote_plus('returnType'): 'JSON'})

    response = urllib.request.urlopen(url).read()
    # json_str = response.read().decode("utf-8")
    json_object = json.loads(response)
    # print(json_object)
    body = json_object['response']
    json_object = body['docs']
    # del json_object['doc']
    # ic(json_object)

    book_list = [json_object[i]['doc'] for i in range(0, len(json_object))]
    # ic(book_list)

    df = pd.DataFrame.from_records(book_list)
    # ic(df)

    df.drop(['addition_symbol', 'class_no', 'loan_count', 'no', 'publication_year', 'ranking', 'vol', 'publisher'],
            axis=1, inplace=True)
    df.columns = ['book_title', 'author', 'isbn', 'category', 'book_img']
    df2json = df.to_json(orient="index")
    df2json = json.loads(df2json)
    for i in range(0, 10):
        book_api_data = list(df2json.values())[i]
    # ic(book_api_data)
    return book_api_data

## /////////////////////////////////////////////////////////////////////
# with open('./data/isbn_books.json', 'r') as file:
#     data = json.load(file)
# # ic(data)
#
# data = sum(data, [])
# # ic(data)
#
# book_list = [data[i]['book'] for i in range(0, len(data))]
# # ic(book_list)
#
# df = pd.DataFrame.from_records(book_list)
# # ic(df)
#
# df.drop(['no', 'publication_date', 'class_no', 'publisher', 'publication_year', 'isbn'], axis=1, inplace=True)
# df.columns = ['book_title', 'author', 'category', 'book_img', 'isbn', 'book_info']
# df2json = df.to_json(orient="index")
# with open('./data/response_json.json', 'w') as f:
#     json.dump(df2json, f)
#
# df2json = json.loads(df2json)
# book_api_data = df2json.values()
# print(book_api_data)
# # with open('../data/processing_data.json', 'w') as f:
# #     json.dump(book_api_data)
#
# with open('./data/test.json', 'w', encoding='utf-8') as f:
#   json.dump(list(book_api_data), f, ensure_ascii=False, indent=4)



