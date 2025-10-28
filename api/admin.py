from django.contrib import admin
from .models import found_items

class FoundItemsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address', 'phone_no', 'keywords', 'description','username','date_created','img'  )

admin.site.register(found_items, FoundItemsAdmin)
