from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('weather/', include('weather_forecast.urls')),
    path('recommendation/', include('recommendation.urls')),
    path('guide/', include('guide.urls')),   

    # Home page - now handled by users.public_dashboard
    path('', include('users.urls')),  # This allows '/' to load the public_dashboard
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
