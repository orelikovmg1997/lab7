from django.contrib import admin
from core import models

@admin.register(models.Service)
class Service(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'price', 'expensive')
    search_fields = ('name', 'price',)

    def get_ordering(self, request):
        return ['price']

    def expensive(self, srv):
        return True if int(srv.price) > 100 else False
