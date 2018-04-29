from django.contrib import admin
from .models import BaseInfo

# Register your models here.
class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ('code','name','url','present_price',
			 'range','price_range','rise_speed',
			 'change_hands','volume_ratio','amplitude',
			 'turnover', 'floating_stock',
			 'circulation_market_value','pe_ratio','create_time','update_time')

admin.site.register(BaseInfo,BaseInfoAdmin)