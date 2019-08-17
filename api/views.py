from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import datetime
import qrcode
import logging as L

# Create your views here.
from rest_framework.authtoken.models import Token
from re import sub


def generate_qr(request):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    data = request.GET['qr_data']
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    filename = "{}{}-{}{}".format(settings.MEDIA_ROOT + 'transactions/qr_codes/',
                                  int(datetime.datetime.now().timestamp()), data, '.png')
    img.save(filename)
    return JsonResponse({'qr_code': '/media/' + filename.split('/media/')[1]})

def get_user_amount(request):
    get_data = request.GET
    token = request.GET['token']
    try:
        token_obj = Token.objects.get(key=token)
        request.user = token_obj.user
    except:
        return JsonResponse({'amount': "0000"})
    return JsonResponse({'amount': str(request.user.amount)})



def add_money(request):
    get_data = request.GET
    token = request.GET['token']
    amount=request.GET['amount']
    try:
        token_obj = Token.objects.get(key=token)
        user = token_obj.user
        user.amount = user.amount + int(amount)
        user.save()
    except:
        pass

    return HttpResponse('ok')

    #
    # header_token = request.META.get('HTTP_AUTHORIZATION', None)
    # if header_token is not None:
    #     try:
    #         token = sub('Token ', '', request.META.get('HTTP_AUTHORIZATION', None))
    #         token_obj = Token.objects.get(key=token)
    #         request.user = token_obj.user
    #     except Token.DoesNotExist:
    #         request.user = None
    #
    # if request.user:
    #
    # return JsonResponse({'error': 'User is anonymous or invalid token'})
