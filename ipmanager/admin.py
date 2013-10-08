from django.contrib import admin
from models import Host


class HostAdmin(admin.ModelAdmin):
    list_display = ('mac', 'ip')

admin.site.register(Host, HostAdmin)
