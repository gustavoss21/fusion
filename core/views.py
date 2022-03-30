from django.shortcuts import render
from django.views.generic import FormView
from .models import Funcionario,Servico,Features
from .forms import ContatoForm
from django.contrib import messages
from django.urls import reverse_lazy

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios'] = Funcionario.objects.all()
        context_lista = Features.objects.all()
        contador = context_lista.count() / 2
        context['features_left'] = context_lista[:contador]
        context['features_right'] = context_lista[contador:]
        context['contador'] = contador
        return context

    def form_valid(self, form,*args,**kwargs):

        form.send_mail()
        messages.success(self.request,'Seu E-mail foi enviado com sucesso')
        return super(IndexView, self).form_valid(form,*args,**kwargs)

    def form_invalid(self, form,*args,**kwargs):
        messages.error(self.request, 'Seu E-mail não foi enviado, tente mais tarde')
        print(1111111111111222)
        return super(IndexView, self).form_valid(form, *args, **kwargs)

# {% for m in messages %}
#            <div class="alert alert-{{ message.tags }}">
#              <button type="button" class="close" data-dismiss="alert"></button>
#              <strong> {{ m }}</strong>
#            </div>
#        {% endfor%}


