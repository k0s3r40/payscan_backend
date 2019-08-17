from django.shortcuts import render

# Create your views here.


def e_shop_test(request):
    return render(request, 'index.html')