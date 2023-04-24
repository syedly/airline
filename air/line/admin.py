from django.contrib import admin
from line.models import contact, book_flight, add_flight
# Register your models here.
admin.site.register(contact)
admin.site.register(book_flight)
admin.site.register(add_flight)