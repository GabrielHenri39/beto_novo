
from django.forms import ModelForm
from django import forms
from .models import Cliente,Agendamento

class TelInput(forms.TextInput):

    input_type = 'tel'
    attrs = {'class':'mask-tel'}

class ClienteFormAdmin(ModelForm):


    def __init__(self, *args,**kwargs):
        super(ClienteFormAdmin,self).__init__(*args,**kwargs)
        self.fields['telefone'].widget.attrs['class'] = 'mask-tel'


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'telefone': TelInput()
        } 
        

class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'data': forms.DateInput(attrs={'class':'form-control'}),
            'horario': forms.TimeInput(attrs={'class':'form-control'}),
        }
        