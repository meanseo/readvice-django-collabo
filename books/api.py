import json
from icecream import ic
import config
import urllib.request
import pandas as pd

# 정보나루 API 및 데이터 정제
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
# ic(json_object)

book_list = [json_object[i]['doc'] for i in range(0, len(json_object))]
# ic(book_list)

df = pd.DataFrame.from_records(book_list)
# ic(df)

df.drop(['addition_symbol', 'class_no', 'loan_count', 'no', 'publication_year', 'ranking', 'vol', 'publisher'], axis=1, inplace=True)
df.columns = ['book_title', 'authors', 'isbn', 'category', 'book_img']
df2json = df.to_json(orient="index")
df2json = json.loads(df2json)
book_api_data = df2json.values()
ic(book_api_data)
