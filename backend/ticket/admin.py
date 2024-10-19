from django.contrib import admin
from ticket.models import Ticket, Category, Tag, Comment, Profile

# Register models here.
admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Profile)