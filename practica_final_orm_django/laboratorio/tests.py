from django.test import TestCase
from django.urls import reverse
from laboratorio.models import Laboratorio

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear datos iniciales para pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Test",
            ciudad="Ciudad Test",
            pais="País Test"
        )

    def test_laboratorio_data(self):
        """
        Verificar que los datos en la base de datos simulada coincidan con los iniciales.
        """
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio Test")
        self.assertEqual(laboratorio.ciudad, "Ciudad Test")
        self.assertEqual(laboratorio.pais, "País Test")

    def test_laboratorio_url(self):
        """
        Verificar que la URL del laboratorio devuelva HTTP 200.
        """
        response = self.client.get(f'/laboratorio/{self.laboratorio.id}/')
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_view_uses_correct_template_and_content(self):
        """
        Verificar:
        - URL devuelve HTTP 200 usando reverse.
        - Se usa la plantilla correcta.
        - El contenido HTML es el esperado.
        """
        response = self.client.get(reverse('laboratorio_detail', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/detail.html')
        self.assertContains(response, "Laboratorio Test")
