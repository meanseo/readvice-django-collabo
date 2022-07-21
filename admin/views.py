from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime


@api_view(['GET'])
def hello_api(request):
    print("####### 서버로 들어옴 #######")
    return Response({'message': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
