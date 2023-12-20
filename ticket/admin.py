from django.contrib import admin
from .models import EnquiryTicket


class EnquiryTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'country',
                    'completion_date', 'budget', 'status')
    list_filter = ('status', 'country')
    search_fields = ('title', 'description', 'user__username')
    date_hierarchy = 'completion_date'


admin.site.register(EnquiryTicket, EnquiryTicketAdmin)
