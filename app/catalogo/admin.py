from django.contrib import admin

from catalogo.models import Sala, Filme, Sessao


class SalaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativa',)
    list_display_links = ('titulo',)
    list_editable = ('ativa',)


class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'duracao', 'indicacao', 'categoria', 
    'em_breve', 'ativo',)
    list_display_links = ('titulo',)
    list_editable = ('ativo','em_breve')
    list_per_page = 15
    actions = ['inativar_filmes',]

    def inativar_filmes(self, request, queryset):
        for filme in queryset:
            """ Inativa filmes selecionados """
            filme.ativo = False
            filme.save(update_fields=['ativo'])
            
    inativar_filmes.short_description = 'Inativar filmes'


class SessaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'ativa',)
    list_display_links = ('__str__',)
    list_editable = ('ativa',)
    list_per_page = 15


admin.site.register(Sala, SalaAdmin)
admin.site.register(Filme, FilmeAdmin)
admin.site.register(Sessao, SessaoAdmin)
