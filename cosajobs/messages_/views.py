from django.shortcuts import render

def test(request):
    
    return render(request,'messages/messages.html')
