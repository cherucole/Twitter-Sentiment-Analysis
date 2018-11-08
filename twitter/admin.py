from django.contrib import admin
from .models import SentimentsTwitterHashtag

# Register your models here.
admin.site.register(SentimentsTwitterHashtag)



# class SentimentsTwitterHashtagAdmin(admin.ModelAdmin):
#     actions = [export_csv, export_xls, export_xlsx]

# admin.site.register(SentimentsTwitterHashtag, SentimentsTwitterHashtagAdmin)
