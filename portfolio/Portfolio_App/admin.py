from django.contrib import admin
from .models import Profilis, Projektas


class ProfilisAdmin(admin.ModelAdmin):
    list_display = ('vardas',
                    'pavarde',
                    'trumpas_prisistatymas',
                    'socialinis_tinklas_linkedin',
                    'socialinis_tinklas_github')

class ProjektasAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas',
                    'aprasymas',
                    'technologiju_sarasas',
                    'projekto_svetaine',
                    'githubo_nuoroda')


admin.site.register(Profilis, ProfilisAdmin)
admin.site.register(Projektas, ProjektasAdmin)