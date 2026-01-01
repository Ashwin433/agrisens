from django import forms

class CropRecommendationForm(forms.Form):
    nitrogen = forms.FloatField(label='Nitrogen (N)', min_value=0, max_value=100)
    phosphorus = forms.FloatField(label='Phosphorus (P)', min_value=0, max_value=100)
    potassium = forms.FloatField(label='Potassium (K)', min_value=0, max_value=100)
    temperature = forms.FloatField(label='Temperature (°C)', min_value=0, max_value=50)
    humidity = forms.FloatField(label='Humidity (%)', min_value=0, max_value=100)
    ph = forms.FloatField(label='pH Level', min_value=0, max_value=14)
    rainfall = forms.FloatField(label='Rainfall (mm)', min_value=0, max_value=500)
