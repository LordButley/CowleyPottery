from django.contrib import admin
from .models import Commission

# Register your models here.

class CommissionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'responded',
    )

admin.site.register(Commission, CommissionAdmin)

