from django.contrib import admin
from .models import *

# Register your models here.


class TableAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Material', 'Height', 'Width', 'Depth', 'In_stock')
    search_fields = ('Name',)
    list_filter = ('Material',)
    list_editable = ('In_stock',)


admin.site.register(Material)
admin.site.register(TableFurniture, TableAdmin)
