''' General views '''

# Django
from django.views.generic import TemplateView

class IndexView(TemplateView):
    ''' Render Index page. '''
    template_name = 'index.html'

class ServicesView(TemplateView):
    ''' Render Services page. '''
    template_name = 'services.html'

class AboutUsView(TemplateView):
    ''' Render About us page. '''
    template_name = 'about_us.html'