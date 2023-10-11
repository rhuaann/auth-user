from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic

from .forms import StandForm
from .models import Stand


# Create your views here.


class StandListView(generic.ListView):
    model = Stand
    paginate_by=2
    template_name = "stand/stands.html"

class StandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Stand
    template_name = "stand/stand_detalhe.html"

class StandCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "stand/form.html"
  
class StandDeleteView(generic.DeleteView):
  model = Stand
  success_url = reverse_lazy("stand_listar")
  template_name = "stand/stand_confirm_delete.html"
  
class StandUpdateView(views.SuccessMessageMixin,generic.UpdateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand_listar")
  success_message= 'Alterações salvas!'
  template_name = "stand/form.html"