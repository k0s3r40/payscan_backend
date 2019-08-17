from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import datetime
import qrcode
import logging as L
from rest_framework.authtoken.models import Token
# Create your views here.

from re import sub


def generate_qr(request):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    data = request.GET['qr_data']
    header_token = request.META.get('HTTP_AUTHORIZATION', None)
    if header_token is not None:
        try:
            token = sub('Token ', '', request.META.get('HTTP_AUTHORIZATION', None))
            token_obj = Token.objects.get(key=token)
            request.user = token_obj.user
        except Token.DoesNotExist:
            request.user = None

    if request.user:
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        filename = "{}{}-{}{}".format(settings.MEDIA_ROOT + 'transactions/qr_codes/',
                                      int(datetime.datetime.now().timestamp()), data, '.png')
        img.save(filename)
        return JsonResponse({'qr_code': '/media/' + filename.split('/media/')[1]})
    return JsonResponse({'error': 'User is anonymous or invalid token'})
