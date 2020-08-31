from django.shortcuts import render

from . models import Status

def status(request):
    statusses = Status.objects.all()
    context={'status':statusses}
    return render(request,'status/status.html',context)
