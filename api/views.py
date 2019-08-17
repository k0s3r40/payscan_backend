from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
import datetime
import qrcode


# Create your views here.



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
    filename = "{}{}-{}{}".format(settings.MEDIA_ROOT+'transactions/qr_codes/',int(datetime.datetime.now().timestamp()), data, '.png')
    img.save(filename)
    return JsonResponse({'qr_code':'/media/'+filename.split('/media/')[1]})

