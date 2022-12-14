from django.contrib import admin

from .models import Veiculo, Cliente, Caracterisca, TipoContrato, Agendar

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'quantidade')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'contrato', 'celular', )

class CaracteristaAdmin(admin.ModelAdmin):

    list_display = ('matricula', 'modelo', 'tipo', 'ano', 'quantidade' )

class TipoContratoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'tipo_contrato', 'faturado', 'ano')

class AgendarAdmin(admin.ModelAdmin):

    list_display = ('cliente', 'contrato', 'data', 'veiculo', 'celular', 'orcamento')


admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Caracterisca, CaracteristaAdmin)
admin.site.register(TipoContrato, TipoContratoAdmin)
admin.site.register(Agendar, AgendarAdmin)
