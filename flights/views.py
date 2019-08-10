from django.views import generic
from .models import Airport, Flight,Passenger
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'flights/index.html'
    context_object_name = 'flights_list'

    def get_queryset(self):
        return Flight.objects.all()

class DetailView(generic.DetailView):
    model = Flight
    template_name = 'flights/details.html'


