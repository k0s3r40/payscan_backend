# users/views.py
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.http import JsonResponse


class CreateUser(generics.CreateAPIView):
    '''CREATES USER WITH POST REQUEST'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)





def get_user_amount(request):
    get_data = request.GET
    token = request.GET['token']
    token_obj = Token.objects.get(key=token)
    request.user = token_obj.user

    return JsonResponse({'amount':str(request.user.amount)})

