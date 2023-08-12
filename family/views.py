from django.shortcuts import render

def myFamily_view(request):
    return render(request, 'family/MyFamily.html')
