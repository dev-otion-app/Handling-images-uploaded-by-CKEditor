from django.views.generic.base import TemplateView
from .models import Post


class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self):
        context = {}
        context['post'] = Post.objects.all()[0]
        return context

