from django.contrib import admin

from .models import Genus, Species

# Register your models here.

class GenusAdmin(admin.ModelAdmin):
    pass

class SpeciesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genus, GenusAdmin)
admin.site.register(Species, SpeciesAdmin)
