from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome',max_length=100)
    email = forms.EmailField(label='E-mail',max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=100)
    mensagem = forms.CharField(label='Sua mensagem',widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'nome: {nome}\nE-mail: {email},Assunto: {assunto}\nMensagem: {mensagem}'
        mail = EmailMessage(subject=assunto,
                            body=conteudo,
                            from_email='santos.gs708@gmail.com',
                            headers={'reply-to':email,},
                            to=['gustavosantos39738@gmail.com',])
        mail.send()