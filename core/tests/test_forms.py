from django.test import TestCase
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')
import django
django.setup()
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'maria'
        self.email = 'santos.gs708@gmail.com'
        self.assunto = 'assunto qualquer'
        self.mensagem = 'mensagem qualquer'
        print(self.email)
        self.dados = {
                     'nome': self.nome,
                     'email': self.email,
                    'assunto': self.assunto,
                    'mensagem': self.mensagem,
                       }
        self.form = ContatoForm(data=self.dados)


    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()
        self.assertEqual(res1,res2)
