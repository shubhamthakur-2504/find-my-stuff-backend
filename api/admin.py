# from django.contrib import admin
# from .models import found_items

# # # Register your models here.
# # @admin.register(users)
# # class userAdmin(admin.ModelAdmin):
# #     list_display=['id','username','password','email']
# # from django.contrib import admin
# # # from .models import users

# class found(admin.ModelAdmin):
#     list_display = ('name','address','phone_no','img','keywords','description','user','date_created')

# # admin.site.register(User, userAdmin)
from django.contrib import admin
from .models import found_items

class FoundItemsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address', 'phone_no', 'keywords', 'description','username','date_created','img'  )

admin.site.register(found_items, FoundItemsAdmin)
