from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')
import django
django.setup()
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome':'fabricio',
            'email':'santosgs@gmail.com',
            'assunto':'teste assunto',
            'mensagem':'teste mensagem',
        }
        self.cliente = Client()
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'),data=self.dados)
        self.assertEqual(request.status_code,302)

    def test_form_invalid(self):
        dados = {
            'nome':'fabricio',
            'mensagem': 'teste mensagem',
        }
        request = self.cliente.post(reverse_lazy('index'),data=dados)
        print(112345433454,'...',request.status_code)
        self.assertEqual(request.status_code,200)