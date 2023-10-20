from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import ReservaForm
from .models import Reserva


class ReservasListView(AdminPermission,LoginRequiredMixin, generic.ListView):
    model = Reserva
    paginate_by=2
    template_name = "reserva/reservas.html"

class ReservaDetailView(AdminPermission,LoginRequiredMixin, generic.DetailView):
    model = Reserva
    template_name = "reserva/reserva_detalhe.html"

class ReservaCreateView(AdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "reserva/form.html"
  
class ReservaDeleteView(AdminPermission,LoginRequiredMixin, generic.DeleteView):
  model = Reserva
  success_url = reverse_lazy("reserva_listar")
  template_name = "reserva/reserva_confirm_delete.html"
  
class ReservaUpdateView(AdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Alterações salvas!'
  template_name = "reserva/form.html"