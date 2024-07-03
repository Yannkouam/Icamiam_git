from django.contrib import admin
from icamapps.models import Product, Order, Event, Panier

# Enregistrement des modèles avec l'administration Django
admin.site.register(Product)
admin.site.register(Event)
admin.site.register(Panier)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'product', 'quantity', 'ordered')
    search_fields = ('order_number', 'user__username', 'product__name')
    list_filter = ('ordered', 'product')
    ordering = ('-ordered',)
