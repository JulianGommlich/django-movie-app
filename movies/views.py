from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

from movies.models import Movie

class MovieView(TemplateView):

    template_name = 'welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context

def delete_movie(request):
    id = request.GET.get('id')
    object = Movie.objects.get(id=id)
    object.delete()
    return HttpResponseRedirect('..')

def add_movie(request):
    name = request.POST.get('movie_name')
    release_year = request.POST.get('release_year')
    genre = request.POST.get('genre')
    movie = Movie(name=name, release_year=release_year, genre=genre, is_available=True)
    movie.save()
    return HttpResponseRedirect('..')