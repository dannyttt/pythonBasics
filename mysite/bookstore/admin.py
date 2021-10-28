from django.contrib import admin
from .models import *


# Register your models here.
class BookManager(admin.ModelAdmin):
    list_display = ["id", "title", "pub", "price", "market_price"]
    ordering = ["id"]
    list_display_links = ["title"]
    # filter
    list_filter = ["pub"]
    # search
    search_fields = ["title"]
    # editable
    list_editable = ["price"]


class AuthorManager(admin.ModelAdmin):
    list_display = ["name", "age", "email"]


admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
admin.site.register(Wife)
