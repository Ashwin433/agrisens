import os
import pickle
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    'recommendation',
    'models',
    'RandomForest.pkl'
)

_model = None

def get_model():
    global _model
    if _model is None:
        with open(MODEL_PATH, 'rb') as model_file:
            _model = pickle.load(model_file)
    return _model


def crop_recommendation_view(request):
    if request.method == 'POST':
        try:
            model = get_model()

            nitrogen = float(request.POST.get('nitrogen', 0))
            phosphorus = float(request.POST.get('phosphorus', 0))
            potassium = float(request.POST.get('potassium', 0))
            temperature = float(request.POST.get('temperature', 0))
            humidity = float(request.POST.get('humidity', 0))
            ph = float(request.POST.get('ph', 0))
            rainfall = float(request.POST.get('rainfall', 0))

            features = [[
                nitrogen, phosphorus, potassium,
                temperature, humidity, ph, rainfall
            ]]

            prediction = model.predict(features)

            return render(request, 'recommendation/crop_recommendation.html', {
                'recommended_crop': prediction[0]
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'recommendation/crop_recommendation.html')
