from django.contrib import admin
from  address_book.models import Person
# Register your models here.
@admin.register(Person)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']