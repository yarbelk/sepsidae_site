from django.contrib import admin

from .models import Contributor, Institution


class ContributorAdmin(admin.ModelAdmin):
    pass

class InstitutionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Institution, InstitutionAdmin)
