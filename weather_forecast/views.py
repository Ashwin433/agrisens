from django.shortcuts import render

def weather_forecast_view(request):
    return render(request, 'weather_forecast/index.html')
