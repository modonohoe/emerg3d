from django.contrib import admin
from .models import EnquiryTicket


class EnquiryTicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'get_user_email', 'country',
                    'completion_date', 'budget', 'status')
    list_filter = ('status', 'country')
    search_fields = ('title', 'description', 'user__username')
    date_hierarchy = 'completion_date'

    # pulls the user's email into the Admin display so they can email them
    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.admin_order_field = 'user__email'
    get_user_email.short_description = 'Email'


admin.site.register(EnquiryTicket, EnquiryTicketAdmin)
