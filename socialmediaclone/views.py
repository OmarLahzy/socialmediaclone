from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class Testpage(TemplateView):
    template_name = 'test.html'

class Thankspage(TemplateView):
    template_name = 'thanks.html'
