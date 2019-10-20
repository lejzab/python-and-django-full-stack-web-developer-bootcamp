from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
    webpages_list = models.AccessRecord.objects.order_by('date')
    context = {'access_records': webpages_list}
    return render(request, 'first_app/index.html',context=context)
