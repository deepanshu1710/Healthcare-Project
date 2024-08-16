from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Assuming you have an 'api' app
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', RedirectView.as_view(url='/admin/', permanent=False)),  # Redirect root URL to admin
]
