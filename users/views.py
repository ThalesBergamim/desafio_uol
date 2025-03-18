from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import UserForm
import requests
import xml.etree.ElementTree as ET
from .models import Users


class RegisterView(View):
    template_name = 'register.html'
    form_class = UserForm

    def get(self, request):
        codename = self._get_codename('L')
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            codename = self._get_codename(form.cleaned_data['group'])
            obj = form.save(commit=False)
            obj.codename = codename
            obj.save()
            return HttpResponse('Cadastro realizado com Sucesso')

        return render(request, self.template_name, {'form': form})

    def _get_codename(self, group):
        if group == 'V':
            response = requests.get('https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/vingadores.json').json()
            codenames = [i['codinome'] for i in response ['vingadores']]
        elif group == 'L':
            response = requests.get('https://raw.githubusercontent.com/uolhost/test-backEnd-Java/master/referencias/liga_da_justica.xml')
            root = ET.fromstring(response.content)
            codenames_element = root.find('codinomes')
            codenames = [codename.text for codename in codenames_element.findall('codinome')]
        
        codenames_used = Users.objects.values_list('codename', flat=True)
        codenames_available = set(codenames) - set(codenames_used)
        
        if not codenames_available:
            return HttpResponse('Não há codinomes disponíveis')
        
        return list(codenames_available)[0]

class ListView(View):
    template_name = "list.html"

    def get(self, request):
        users = Users.objects.all()
        return render(request, self.template_name, {'users': users})        
            
            