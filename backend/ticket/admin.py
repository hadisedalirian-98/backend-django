from django.contrib import admin
from ticket.models import Ticket, Category, Tag, Profile, TicketConversation

# Register models here.
admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(TicketConversation)