from django.contrib import admin
from .models import CreditOffer


@admin.register(CreditOffer)
class CreditOfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'term', 'grace_period')
    search_fields = ('amount', 'term')
    list_filter = ('term',)
    fields = (
        'logo',
        'name',
        'amount',
        'term',
        'grace_period',
        'apply_url',
        'details_text',
    )
