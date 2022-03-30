from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação',auto_now_add=True)
    modificados = models.DateField('Atualizado',auto_now=True)
    ativo = models.BooleanField('Ativo',default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
                        ('lni-cog','Engrenagem'),
                        ('lni-stats-up','Gráfico'),
                        ('lni-users','Usuários'),
                        ('lni-layers','Design'),
                        ('lni-mobile','Mobile'),
                        ('lni-rocket','Foquete'),
                    )

    servico = models.CharField('Serviço',max_length=100)
    descricao = models.TextField('Descriçao',max_length=200)
    icone = models.CharField('Icone',max_length=12,choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo',max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo',verbose_name='Cargo',on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem',upload_to=get_file_path,variations={'thub':{'width':480,'height':480,'crop':True}})
    faceboock = models.CharField('Faceboock',max_length=100,default='#')
    instagram = models.CharField('instagram',max_length=100,default='#')
    instagram = models.CharField('twitter',max_length=100,default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome


# class Comentario(Base):
#         nome = models.CharField('Nome',max_length=100)
#         email = models.EmailField('E-mail',max_length=100)
#         objetivo = models.CharField('Objetivo')
#         mensagem = models.TextField('Mensagem',max_length=200)

class Features(Base):
    ICONE_CHOICES = (
                        ('lni-rocket','turbine'),
                        ('lni-laptop-phone','repositorio'),
                        ('lni-cog','engrenagem'),
                        ('lni-leaf','design'),
                        ('lni-layers','camada'),
                        ('lni-leaf','formulario'),
                    )

    feature = models.CharField('Feature',max_length=100)
    descricao = models.TextField('Descriçao',max_length=200)
    icone = models.CharField('Icone',max_length=16,choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.feature
