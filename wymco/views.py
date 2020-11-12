''' General views '''

# Django
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class ServicesView(TemplateView):
    template_name = 'services.html'

class AboutUsView(TemplateView):
    template_name = 'about_us.html'