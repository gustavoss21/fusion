import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')
import django
django.setup()
from django.test import TestCase
from model_mommy import mommy
import uuid

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self):

        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None,'teste.png')
        self.assertTrue(len(arquivo),len(self.filename))

class FeaturesTestCase(TestCase):
    def setUp(self):
        self.feature = mommy.make('Features')

    def test_str(self):
        self.assertEquals(str(self.feature), self.feature.feature)

class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')

    def test___str___(self):
        self.assertEquals(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(str(self.cargo)), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(str(self.funcionario)), self.funcionario.nome)