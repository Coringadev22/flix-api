from django.contrib import admin
from movies.models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ['name']  # Permite buscar pelo nome
