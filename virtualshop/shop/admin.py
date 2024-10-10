from django.contrib import admin

# Register your models here.

from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome','slug']
    prepopulated_fields = {'slug':('nome',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display=[
        'nome','slug','preco','disponivel','criado','atualizado'
        ]
    list_filter = ['disponivel','criado','atualizado']
    list_editable = ['preco','disponivel']
    prepopulated_fields = {'slug':('nome',)}
