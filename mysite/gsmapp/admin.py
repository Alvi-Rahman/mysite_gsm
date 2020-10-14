from django.contrib import admin
from gsmapp import models

# Register your models here.

class BrandInfoAdmin(admin.ModelAdmin):
    list_display = ['brand_name','brand_img','is_popular','added_date','status']
    search_fields  = ['brand_name']
    list_filter  = ['brand_name','is_popular','status']

class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['product_name','brand_name','product_img','added_date','update_date','status']
    search_fields  = ['brand_name']
    list_filter  = ['brand_name','status']

class BlogInfoAdmin(admin.ModelAdmin):
    list_display = ['blog_title','use_slider','added_date','status']
    search_fields  = ['blog_title']
    list_filter  = ['status']

admin.site.register(models.CategoryInfo)
admin.site.register(models.BrandInfo, BrandInfoAdmin)
admin.site.register(models.ProductInfo, ProductInfoAdmin)
admin.site.register(models.SliderInfo)
admin.site.register(models.ProductThreeDView)
admin.site.register(models.ProductReview)
admin.site.register(models.ProductPricing)
admin.site.register(models.SubscribeEmail)
admin.site.register(models.BlogComments)
admin.site.register(models.ProductWiseUserComment)
admin.site.register(models.BlogInfo, BlogInfoAdmin)