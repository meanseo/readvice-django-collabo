import requests
import json

from icecream import ic

import config
import urllib.request
from urllib.parse import urlencode, quote_plus, unquote
import pandas as pd
from pandas.io.json import json_normalize


SUBSCRIPTION_KEY = config.data_book_api_key
# url2 = f'http://data4library.kr/api/libSrchByBook?authKey={config.data_book_api_key}&isbn=[ISBN]&region=[지역코드]'
url = f'http://data4library.kr/api/loanItemSrch?authKey={config.data_book_api_key}&startDt=2022-07-10&endDt=2022-07-12&format=json'
# queryParams = '&' + urlencode({quote_plus('page'): '1', quote_plus('perPage'): '1824', quote_plus('returnType'): 'JSON'})

response = urllib.request.urlopen(url).read()

# json_str = response.read().decode("utf-8")

json_object = json.loads(response)

body = json_object['response']

json_object = body['docs']

# del json_object['doc']

ic(json_object)

# print(type(json_object))
# print(json_object[0].keys)

# book_list=[]

book_list = [json_object[i]['doc'] for i in range(0, len(json_object))]
ic(book_list)

df = pd.DataFrame.from_records(book_list)
ic(df)

df.drop(['addition_symbol', 'class_no', 'loan_count', 'no', 'publication_year', 'ranking', 'vol', 'publisher'], axis=1, inplace=True)
df.columns = ['book_title', 'authors', 'isbn', 'category', 'book_img']
df = df.to_json(orient="index")
json_object = json.loads(df)
a = json_object.values()
ic(a)

# df.to_csv('./save/book_list.csv', index=False)
# dataframe = json_normalize(json_object)
# print(dataframe)
# file = open('book.json', "w+")
# file.write(json.dumps(json_object))