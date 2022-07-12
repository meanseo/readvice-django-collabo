from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from .models import  User
from .serializers import UserSerializer
from rest_framework.response import Response

@api_view(["GET", "POST", "PUT", "DELETE"])
@parser_classes([JSONParser])
def users(request):
    print('1 users 로 들어옴')
    try:
        if request.method == 'GET':
            print('2 GET 으로 들어옴')
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            print(f'2 POST 로 들어옴')
            # print('request_data: ', request.data)
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):  # raise된 에러를 가시적으로 클라이언트에 전달
                # print(serializer)
                # print('3. 들어온 내부값: ', serializer.data)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print('error: ', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'PUT':
            print('2 PUT 으로 들어옴')
            users = User.objects.all()
            serializer = UserSerializer(users, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            users = User.objects.all()
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@parser_classes([JSONParser])
def login(request):
    print(f'1 login 로 들어옴')
    email = request.data.get('email')  # 클라이언트 요청 이메일
    password = request.data.get('password') # 클라이언트 요청 패스워드
    try:
        if email == User.objects.get(email=email).email: # 클라이언트 이메일 == db 이메일
            if password == User.objects.get(email=email).password: # 클라이언트 패스워드 == db 패스워드 (클라이언트 이메일과 일치하는 패스워드를 가져옴)
                return Response({"Message": "로그인 성공"})
            else:
                return Response({"Message": "비밀번호 오류"})
    except User.DoesNotExist:
        return Response({"Message": "존재 하지 않는 아이디"})