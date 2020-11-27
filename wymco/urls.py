''' Wymco URLs modules. '''

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Views
from . import views as general_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # General views
    path('', general_views.IndexView.as_view(), name='index'),
    path('services', general_views.ServicesView.as_view(), name='services'),
    path('about_us', general_views.AboutUsView.as_view(), name='about-us'),

    # Blog views
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)