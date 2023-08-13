from django.contrib import admin
from .models import Contact, New

# Register your models here.
#class NewAdmin(admin.ModelAdmin):
#    list_display = ('title', 'select_category', 'feed_url')
#    prepopulated_fields = {"feed_url": ("title",)}

#class ContactAdmin(admin.ModelAdmin):
#    list_display = ('name', 'email', 'phone')


admin.site.register(Contact)
admin.site.register(New)