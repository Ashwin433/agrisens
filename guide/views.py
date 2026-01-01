from django.shortcuts import render

def smart_farming_guide(request):
    return render(request, 'guide/index.html')
