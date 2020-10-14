from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class CategoryInfo(models.Model):
    cat_name      = models.CharField(max_length=150, unique=True) 
    cat_url       = models.CharField(max_length=250, blank=True, null=True) 
    ordering      = models.IntegerField(default=0)
    added_date    = models.DateTimeField(auto_now_add=True)
    status        = models.BooleanField(default=True)

    def __str__(self):
        return self.cat_name

class BrandInfo(models.Model):
    brand_name    = models.CharField(max_length=150, unique=True)
    brand_img     = models.ImageField(upload_to="brand", blank=True)  
    img_alt_tag   = models.TextField(blank=True, null=True)
    page_title    = models.TextField(blank=True, null=True)
    meta_title    = models.CharField(max_length=200, blank=True, null=True)
    meta_des      = models.CharField(max_length=250, blank=True, null=True)
    ordering      = models.IntegerField(default=0)
    added_date    = models.DateTimeField(auto_now_add=True)
    is_popular    = models.BooleanField(default=False)
    status        = models.BooleanField(default=True)

    def __str__(self):
        return self.brand_name

class SliderInfo(models.Model):
    slider_name   = models.CharField(max_length=150, unique=True)
    slider_details = models.TextField(blank=True, null=True)
    slider_img    = models.ImageField(upload_to="slider", blank=True)
    img_alt_tag   = models.TextField(blank=True, null=True)
    page_title    = models.TextField(blank=True, null=True)
    ordering      = models.IntegerField(default=0)
    added_date    = models.DateTimeField(auto_now_add=True)
    status        = models.BooleanField(default=True)

    def __str__(self):
        return self.slider_name

class BlogInfo(models.Model):
    cat_name      = models.ForeignKey(CategoryInfo, on_delete=models.CASCADE, blank=True, null=True)
    short_title   = models.CharField(max_length=150, blank=True, null=True)
    blog_title    = models.CharField(max_length=250, unique=True)
    meta_title    = models.CharField(max_length=200, blank=True, null=True)
    meta_des      = models.CharField(max_length=250, blank=True, null=True)
    img_alt_tag   = models.TextField(blank=True, null=True)
    page_title    = models.TextField(blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    source        = models.TextField(blank=True, null=True)
    blog_slug     = models.TextField(blank=True, null=True)
    blog_details  = RichTextField()
    blog_img      = models.ImageField(upload_to="blog", blank=True)
    latest_news   = models.BooleanField(default=False)
    ordering      = models.IntegerField(default=0)
    use_slider    = models.BooleanField(default=False)
    added_date    = models.DateTimeField(auto_now_add=True)
    update_date   = models.DateTimeField(auto_now=True)
    status        = models.BooleanField(default=True)

    def __str__(self):
        return self.blog_title

class ProductInfo(models.Model):
    cat_name           = models.ForeignKey(CategoryInfo, on_delete=models.CASCADE, blank=True, null=True)  
    meta_title         = models.CharField(max_length=200, blank=True, null=True)
    meta_des           = models.CharField(max_length=250, blank=True, null=True)
    og_description     = models.TextField(blank=True, null=True)
    img_alt_tag        = models.TextField(blank=True, null=True)
    page_title         = models.TextField(blank=True, null=True)
    display_size_top   = models.CharField(max_length=100, blank=True, null=True)
    display_resolution_top = models.CharField(max_length=100, blank=True, null=True)
    camera_photo_pixel_top = models.CharField(max_length=100, blank=True, null=True)
    camera_video_pixel_top = models.CharField(max_length=100, blank=True, null=True)
    reviews_top = models.CharField(max_length=100, blank=True, null=True)
    ram_top     = models.CharField(max_length=100, blank=True, null=True)
    chipset_top = models.CharField(max_length=100, blank=True, null=True)
    battery_capacity_top   = models.CharField(max_length=100, blank=True, null=True)
    battery_technology_top = models.CharField(max_length=100, blank=True, null=True)
    specifications_top     = models.TextField(blank=True, null=True)
    overview_title     = models.TextField(blank=True, null=True)
    brand_name         = models.ForeignKey(BrandInfo, on_delete = models.CASCADE)
    product_name       = models.CharField(max_length=150)
    product_model      = models.CharField(max_length=50, blank=True, null=True)
    product_img        = models.ImageField(upload_to="product_img", blank=True)
    network_technology = models.CharField(max_length=250, blank=True, null=True)
    network_2g_bands   = models.CharField(max_length=250, blank=True, null=True)
    network_3g_bands   = models.CharField(max_length=250, blank=True, null=True)
    network_4g_bands   = models.CharField(max_length=250, blank=True, null=True)
    network_5g_bands   = models.CharField(max_length=250, blank=True, null=True)
    network_speed      = models.CharField(max_length=250, blank=True, null=True)
    launch_announced   = models.CharField(max_length=80, blank=True, null=True)
    launch_status      = models.CharField(max_length=250, blank=True, null=True)
    body_dimensions    = models.CharField(max_length=250, blank=True, null=True)
    body_weight        = models.CharField(max_length=250, blank=True, null=True)
    body_build         = models.CharField(max_length=250, blank=True, null=True)
    body_sim           = models.CharField(max_length=250, blank=True, null=True)
    display_type       = models.CharField(max_length=250, blank=True, null=True)
    display_size       = models.CharField(max_length=250, blank=True, null=True)
    display_resolution = models.CharField(max_length=250, blank=True, null=True)
    display_protection = models.CharField(max_length=250, blank=True, null=True)
    platform_os        = models.CharField(max_length=250, blank=True, null=True)
    platform_chipset   = models.CharField(max_length=250, blank=True, null=True)
    platform_cpu       = models.CharField(max_length=250, blank=True, null=True)
    platform_gpu       = models.CharField(max_length=250, blank=True, null=True)
    memory_card_slot   = models.CharField(max_length=250, blank=True, null=True)
    memory_internal    = models.CharField(max_length=250, blank=True, null=True)
    main_camera_type   = models.CharField(max_length=250, blank=True, null=True)
    main_cam_type_des  = models.CharField(max_length=250, blank=True, null=True)
    main_camera_features = models.CharField(max_length=150, blank=True, null=True)
    main_camera_video  = models.CharField(max_length=250, blank=True, null=True)
    selfie_camera_type = models.CharField(max_length=150, blank=True, null=True)
    selfie_cam_type_des = models.CharField(max_length=250, blank=True, null=True)
    selfie_camera_features = models.CharField(max_length=150, blank=True, null=True)
    selfie_camera_video    = models.CharField(max_length=150, blank=True, null=True)
    sound_loudspeaker  = models.CharField(max_length=150, blank=True, null=True)
    sound_3_5mm_jack   = models.CharField(max_length=50, blank=True, null=True)
    comms_wlan         = models.CharField(max_length=250, blank=True, null=True)
    comms_bluetooth    = models.CharField(max_length=250, blank=True, null=True)
    comms_gps          = models.CharField(max_length=250, blank=True, null=True)
    comms_nfc          = models.CharField(max_length=250, blank=True, null=True)
    comms_radio        = models.CharField(max_length=250, blank=True, null=True)
    comms_usb          = models.CharField(max_length=250, blank=True, null=True)
    features_sensors   = models.CharField(max_length=250, blank=True, null=True)
    battery_type       = models.CharField(max_length=250, blank=True, null=True)
    battery_description = models.CharField(max_length=250, blank=True, null=True) 
    battery_charging   = models.CharField(max_length=250, blank=True, null=True) 
    battery_talk_time  = models.CharField(max_length=150, blank=True, null=True) 
    battery_music_play = models.CharField(max_length=150, blank=True, null=True) 
    misc_colors        = models.CharField(max_length=250, blank=True, null=True)
    misc_models        = models.CharField(max_length=250, blank=True, null=True)
    misc_sar           = models.CharField(max_length=250, blank=True, null=True)
    misc_sar_eu        = models.CharField(max_length=250, blank=True, null=True)
    price              = models.CharField(max_length=250, blank=True, null=True)
    bd_price           = models.CharField(max_length=250, blank=True, null=True)
    disclaimer         = models.CharField(max_length=250, blank=True, null=True)
    test_performance   = models.CharField(max_length=250, blank=True, null=True)
    test_display       = models.CharField(max_length=250, blank=True, null=True)
    test_camera        = models.CharField(max_length=250, blank=True, null=True)
    test_battery_life  = models.CharField(max_length=250, blank=True, null=True)
    total_view         = models.IntegerField(default=0)
    added_date         = models.DateTimeField(auto_now_add=True)
    update_date        = models.DateTimeField(auto_now=True)
    ordering           = models.IntegerField(default=0)
    latest_device      = models.BooleanField(default=False) 
    status             = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

class ProductThreeDView(models.Model):
    product_name  = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, blank=True, null=True)
    three_d_img   = models.ImageField(upload_to="product_3d_view", blank=True) 
    img_alt_tag   = models.TextField(blank=True, null=True)
    ordering      = models.IntegerField(default=0)
    added_date    = models.DateTimeField(auto_now_add=True)
    status        = models.BooleanField(default=True)

    def __str__(self):
        return str(self.three_d_img)

class ProductReview(models.Model):
    product_name   = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, blank=True, null=True)
    review_video   = models.TextField(blank=True, null=True)
    review_details = RichTextField()
    added_date     = models.DateTimeField(auto_now_add=True)
    update_date    = models.DateTimeField(auto_now=True)
    status         = models.BooleanField(default=True)

    def __str__(self):
        return str(self.product_name)

class ProductPricing(models.Model):
    product_name   = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, blank=True, null=True)
    device_title   = models.CharField(max_length=200, blank=True, null=True)
    site_image     = models.ImageField(upload_to="product_pricing", blank=True, null=True) 
    img_alt_tag    = models.TextField(blank=True, null=True)
    site_link      = models.TextField(blank=True, null=True)
    dollar_price   = models.FloatField(default=0)
    euro_price     = models.FloatField(default=0)
    rupee_price    = models.FloatField(default=0)
    bd_price       = models.FloatField(default=0)
    added_date     = models.DateTimeField(auto_now_add=True)
    update_date    = models.DateTimeField(auto_now=True)
    status         = models.BooleanField(default=True)

    def __str__(self):
        return str(self.device_title)
    
class SubscribeEmail(models.Model): 
    subscribe_email = models.CharField(max_length=150, unique = True)   
    ip_address      = models.CharField(max_length=150, blank=True, null=True)   
    added_date      = models.DateTimeField(auto_now_add=True)
    status          = models.BooleanField(default=True)

    def __str__(self):
        return str(self.subscribe_email)
    
    
class BlogComments(models.Model): 
    blog_name       = models.ForeignKey(BlogInfo, on_delete=models.CASCADE)
    full_name       = models.CharField(max_length=70)   
    user_email      = models.CharField(max_length=150, blank=True, null=True)   
    user_comment    = models.TextField()
    ip_address      = models.CharField(max_length=150, blank=True, null=True)   
    added_date      = models.DateTimeField(auto_now_add=True)
    status          = models.BooleanField(default=False)

    def __str__(self):
        return str(self.blog_name)
        
class ProductWiseUserComment(models.Model): 
    product_name    = models.ForeignKey(ProductInfo, on_delete=models.CASCADE)
    full_name       = models.CharField(max_length=70)   
    user_email      = models.CharField(max_length=150, blank=True, null=True)   
    user_comment    = models.TextField()
    ip_address      = models.CharField(max_length=150, blank=True, null=True)   
    added_date      = models.DateTimeField(auto_now_add=True)
    status          = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product_name)

class ProductPermalink(models.Model):
    id              = models.AutoField(primary_key=True)
    content         = models.IntegerField(default=0)  
    info_type       = models.CharField(max_length=150)
    permalink       = models.CharField(max_length=150)
    redirect_url    = models.CharField(max_length=255)  
    
    
    