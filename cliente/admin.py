from django.contrib import admin
from django.conf import settings
from .models import Cliente,Agendamento
from .forms import ClienteFormAdmin

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    form = ClienteFormAdmin

    class Media:
        js = (
            settings.STATIC_URL + 'geral/js/jquery.mask.min.js',
            settings.STATIC_URL + 'geral/js/custom.js',
        )


 
@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):


    list_display = ['cliente', 'data_displey','horario','status']
    list_filter = ['cliente','data','horario','status']
    list_editable = ['status']  
    search_fields = ['cliente__nome']


    def data_displey(self, agendamento):
        if agendamento.data:
            return agendamento.data.strftime('%d/%m/%Y')
    

    

    def horario (self, agendamento):
        return agendamento.horario.strftime('%H:%M')


    def status(self, agendamento):
        return agendamento.status.nome
    
    