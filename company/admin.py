from django.contrib import admin
from models import Company, Product


class CompanyAdminList(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'schedule_start',
        'schedule_end',
        'schedule_weekdays',
        'phone_number',
        'email',
        'map_link',
        'social_media1',
        'social_media2',
        'social_media3',
    ]


class ProductAdminList(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'created_at',
        'updated_at',
        'price',
        'discount',
        'quantity',
        'company',
    ]


admin.site.register(Company, CompanyAdminList)
admin.site.register(Product, ProductAdminList)

admin.site.site_header = 'REVIRO Admin'
admin.site.index_title = 'REVIRO Internship Admin Page'
admin.site.site_title = 'REVIRO Internship Admin'
