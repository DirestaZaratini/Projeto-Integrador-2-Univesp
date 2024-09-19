from django.contrib import admin
from .models import Concurso, Examinador, Prova, Candidato, Nota


class ExaminadorInline(admin.TabularInline):
    model = Examinador
    extra = 1


class ProvaInline(admin.TabularInline):
    model = Prova
    extra = 1


@admin.register(Concurso)
class ConcursoAdmin(admin.ModelAdmin):
    inlines = [ExaminadorInline, ProvaInline]


@admin.register(Prova)
class ProvaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'concurso', 'eliminatoria', 'peso', 'num_pessoas']


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'prova']


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ['candidato', 'examinador', 'nota']

