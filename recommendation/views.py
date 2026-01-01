import pickle
from django.shortcuts import render
from django.http import JsonResponse

# Load your trained model (update the path if needed)
MODEL_PATH = 'C:/Users/ashwi/agrisens/recommendation/models/RandomForest.pkl'

with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

def crop_recommendation_view(request):
    if request.method == 'POST':
        try:
            # Extract features from form data (request.POST)
            nitrogen = float(request.POST.get('nitrogen', 0))
            phosphorus = float(request.POST.get('phosphorus', 0))
            potassium = float(request.POST.get('potassium', 0))
            temperature = float(request.POST.get('temperature', 0))
            humidity = float(request.POST.get('humidity', 0))
            ph = float(request.POST.get('ph', 0))
            rainfall = float(request.POST.get('rainfall', 0))

            # Prepare feature array
            features = [[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]]

            # Make prediction using ML model
            prediction = model.predict(features)

            return render(request, 'recommendation/crop_recommendation.html', {
                'recommended_crop': prediction[0]
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    # Initial GET request shows the form only
    return render(request, 'recommendation/crop_recommendation.html')
