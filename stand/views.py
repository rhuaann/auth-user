from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from django_filters.views import FilterView

from .filters import StandFilter
from .forms import StandForm
from .models import Stand


# Create your views here.


class StandListView(LoginRequiredMixin,generic.ListView,FilterView):
    model = Stand
    paginate_by = 5
    ordering = ["-created_at"]
    filterset_class = StandFilter
    template_name = "stand/stands.html"

    def get_queryset(self):
        return Stand.objects.filter(created_by=self.request.user)

class StandDetailView(LoginRequiredMixin, generic.DetailView):
    model = Stand
    template_name = "stand/stand_detalhe.html"

class StandCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  success_url = reverse_lazy("stand_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "stand/form.html"

  def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
  
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


from django.shortcuts import render
from django.core.paginator import Paginator, Page

# def filtro_localizacao(request):
#     # localizacao = request.GET.get('localizacao', '')  # Obter o valor da categoria da URL
    
#     # localizacoes_filtrados = Stand.objects.all()

#     # if localizacao:
#     #     localizacoes_filtrados = localizacoes_filtrados.filter(localizacao=localizacao)

#     # return render(request, 'stand/stands.html', {'localizacoes_filtrados': localizacoes_filtrados})

#     termo = request.GET.get('termo', '')
#     localizacoes = Stand.objects.order_by('localizacao')

#     if termo:
#         localizacoes = localizacoes.filter(localizacao__icontains=termo)

#     return render(request, 'stand/stands.html', {'localizacoes': localizacoes, 'termo': termo})

# def filtro_valores(request):
#     termo = request.GET.get('termo', '')
#     ordenacao = request.GET.get('ordenacao', 'asc')  # Padrão para ordem crescente
#     ordenacao = 'valor' if ordenacao == 'asc' else '-valor'  # Reverter para ordem decrescente se necessário
#     itens = Stand.objects.order_by(ordenacao)

#     if termo:
#         itens = itens.filter(valor__icontains=termo)
#         itens = itens.filter(localizacao__icontains=termo)

#     return render(request, 'stand/stands.html', {'itens': itens, 'termo': termo, 'ordenacao': ordenacao})


def filtro_localizacoes_e_valores(request):
    termo_localizacao = request.GET.get('termo_localizacao', '')
    termo_valor = request.GET.get('termo_valor', '')
    ordenacao = request.GET.get('ordenacao', 'asc')  # Padrão para ordenação crescente
    ordenacao_valor = 'valor' if ordenacao == 'asc' else '-valor'  # Reverter para ordenação decrescente, se necessário
    itens = Stand.objects.order_by(ordenacao_valor)

    if termo_localizacao:
        itens = itens.filter(localizacao__icontains=termo_localizacao)

    if termo_valor:
        itens = itens.filter(valor__icontains=termo_valor)

    paginator = Paginator(itens, 5)  # 10 itens por página (você pode ajustar isso)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'stand/stands.html', {
        'itens': page,
        'termo_localizacao': termo_localizacao,
        'termo_valor': termo_valor,
        'ordenacao': ordenacao,
    })