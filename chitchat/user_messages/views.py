from django.shortcuts import render

# Create your views here.

def messages(request):
    return render(request,'messages/messages.html')