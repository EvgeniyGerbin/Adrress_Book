from address_book.models import Person
from address_book.forms import PersonForm
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.db.models import Q

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    success_url = '/'
    template_name = 'person/create_person.html'

class PersonPageView(ListView):
    model = Person
    template_name = 'base.html'


class PersonUpdateView(UpdateView):
    success_url = '/'
    model = Person
    fields = '__all__'
    template_name = 'person/update_person.html'

class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'person/delete_person.html'
    success_url = '/'


class Search(ListView):
    model = Person
    template_name = 'base.html'

    def get_queryset(self):
        return Person.objects.filter(Q(first_name__icontains=self.request.GET.get("q")) |
                                     Q(last_name__icontains=self.request.GET.get("q")))

