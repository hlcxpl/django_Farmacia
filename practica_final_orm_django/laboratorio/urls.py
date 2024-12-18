from django.urls import path
from .views import (  # Importa todas las vistas necesarias
    LaboratorioListView,
    LaboratorioCreateView,
    LaboratorioDetailView,
    LaboratorioUpdateView,
    LaboratorioDeleteView,
)

urlpatterns = [
    path('', LaboratorioListView.as_view(), name='laboratorio_list'),
    path('nuevo/', LaboratorioCreateView.as_view(), name='laboratorio_create'),
    path('<int:pk>/', LaboratorioDetailView.as_view(), name='laboratorio_detail'),
    path('<int:pk>/editar/', LaboratorioUpdateView.as_view(), name='laboratorio_edit'),
    path('<int:pk>/eliminar/', LaboratorioDeleteView.as_view(), name='laboratorio_delete'),
    
]
