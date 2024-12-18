from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from .models import Laboratorio


# Vista Detalle
class LaboratorioDetailView(DetailView):
    model = Laboratorio
    template_name = 'laboratorio/detail.html'
    context_object_name = 'laboratorio'

# Lista de laboratorios
class LaboratorioListView(ListView):
    model = Laboratorio
    template_name = 'laboratorio/list.html'
    context_object_name = 'laboratorios'

class LaboratorioCreateView(CreateView):
    model = Laboratorio
    template_name = 'laboratorio/form.html'
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorio_list')

    def form_valid(self, form):
        print(form.cleaned_data)  # Depura para verificar los datos procesados
        return super().form_valid(form)


class LaboratorioUpdateView(UpdateView):
    model = Laboratorio
    template_name = 'laboratorio/form.html'
    fields = ['nombre', 'ciudad', 'pais']
    success_url = reverse_lazy('laboratorio_list')

    def form_valid(self, form):
        print(form.cleaned_data)  # Depura para verificar los datos procesados
        return super().form_valid(form)

# Eliminar un laboratorio
class LaboratorioDeleteView(DeleteView):
    model = Laboratorio
    template_name = 'laboratorio/confirm_delete.html'
    success_url = reverse_lazy('laboratorio_list')
