from django.contrib import admin

# Register your models here.
from touchpoint.models import Touchpoint


class TouchpointAdmin(admin.ModelAdmin):    
    list_display = ('id', 'username', 'modified_date', 'status', 'rule_approved')
    list_filter = ('status', 'modified_date')        


admin.site.register(Touchpoint, TouchpointAdmin)