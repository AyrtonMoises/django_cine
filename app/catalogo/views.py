from django.views.generic import ListView

from catalogo.models import Filme


class HomeListView(ListView):
    model = Filme
    template_name = "catalogo/home/index.html"
    context_object_name = 'filmes'

    def get_queryset(self):
        queryset = {
            'em_breve': Filme.objects.filter(em_breve=True), 
            'em_cartaz': Filme.objects.all()
        }
        return queryset