from django.shortcuts import render

# Create your views here.

def bookmarks(request):
    return render(request,'bookmarks/bookmarks.html')