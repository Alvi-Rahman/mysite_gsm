from django import template
from gsmapp import models

register = template.Library()


@register.filter(name='get_brand')
def brand_list(obj):
    try:
        brand = models.BrandInfo.objects.filter(is_popular = True, status = True).order_by("ordering")[:39]
        return brand
    except:
        return None

@register.filter(name='daily_interest_product')
def daily_interest_product(obj):
    try:
        daily_interest = models.ProductInfo.objects.filter(status = True).order_by("-total_view")[:10]
        return daily_interest
    except:
        return None

@register.filter(name='brand_device_count')
def brand_device_count(obj):
    try:
        brand_device = models.ProductInfo.objects.filter(brand_name_id = obj, status = True).count()
        return brand_device
    except:
        return None

@register.filter(name='category_list')
def category_list(obj):
    try:
        category = models.CategoryInfo.objects.filter(status = True)
        return category
    except:
        return None

@register.filter(name='blog_details')
def blog_details(obj):
    try:
        return obj.replace('\n', '<br>')
    except:
        return None

