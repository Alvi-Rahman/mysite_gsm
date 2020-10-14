from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse, HttpResponse , HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from gsmapp import models
from django.utils import timezone
from django.db.models import F
from datetime import datetime
from django.urls import reverse
# import youtube_dl
from PIL import Image
import os, hashlib, json

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = 'sumon2020$gsmridersdb'
)

mycursor = mydb.cursor()

# Create your views here.

def sitemap(request): 
    return render(request, "gsmapp/pages/sitemap.xml")
    
def home_page(request):
    slider_list = models.BlogInfo.objects.filter(use_slider = True, status = True).order_by('-added_date','ordering')[:5]
    latest_device = models.ProductInfo.objects.filter(latest_device = True, status = True).order_by('-update_date','-added_date')[:16]
    latest_news = models.BlogInfo.objects.filter(latest_news = True, status = True).order_by('-update_date','-added_date','ordering')
    context = {
        'static_file':settings.STATIC_ROOT,
        'slider_list': slider_list,
        'latest_device': latest_device,
        'latest_news': latest_news,
        'current_datetime': timezone.now()
    }
    return render(request, "gsmapp/pages/index.html", context) 

def search_data_ajax(request):

    blog_list = []
    if request.method == 'GET':
        myresult =  models.ProductInfo.objects.all()[:3]
        tmp = []
            
        for x in myresult:
            tmp.append([x.product_img,x.product_name,x.pk])
            
    if request.method == 'POST':
        if 'data' in request.POST.keys():
            myresult = models.ProductInfo.objects.filter(product_name__icontains=request.POST['data'])

            tmp = []
            if len(myresult)>3:
                for x in myresult[:3]:
                    tmp.append([x.product_img,x.product_name,x.pk])
            else:
                for x in myresult[:5]:
                    tmp.append([x.product_img,x.product_name,x.pk])
        

    return JsonResponse(json.dumps(tmp,default=str),safe=False)


def brand(request):
    brand_list = models.BrandInfo.objects.filter(status = True).order_by("brand_name")
    context = {
        'brand_list': brand_list
    }
    return render(request, "gsmapp/pages/brand.html", context) 

def brand_wise_product(request, brand_name):
    product_list = models.ProductInfo.objects.filter(brand_name_id__brand_name__iexact = brand_name, status = True)
    if product_list:
        page_title = product_list[0].brand_name.page_title
    else:
        page_title = brand_name

    context = {
        'product_list': product_list,
        'brand_name': brand_name.upper(),
        'page_title': page_title,
    }
    return render(request, "gsmapp/pages/brand_wise_product.html", context)

def get_next_product(request):
    if request.is_ajax:
        brand_id   = request.POST.get("brand")
        current_no = request.POST.get("count")
        product_list = models.ProductInfo.objects.filter(brand_name_id__brand_name__iexact = brand_id, status = True)[:12]
    
        dic = {'name': brand_id }
        return HttpResponse(json.dumps(dic), content_type='application/json')


# ====================Compare AJAX LINK====================

def compare_product(request):
    
    if request.method == 'GET':
        prod =  models.ProductInfo.objects.all()

    if request.method == 'POST':
        prod = models.ProductInfo.objects.filter(pk = request.POST['data'])
        prod = list(prod.values())
    return JsonResponse(json.dumps(prod,default=str),safe=False)



# =====================Direct Links============================

def direct_details(request, name):
    
    if request.method == "GET":

        perma = models.ProductPermalink.objects.filter(permalink=name)[0]
        if perma.info_type == 'blog':
            blog_details = models.BlogInfo.objects.filter(blog_slug = name, status = True).first() 
            related_blog_post = models.BlogInfo.objects.filter(status = True).order_by("-added_date")[:4]
            user_blog_comments = models.BlogComments.objects.filter(status = True).order_by("-added_date")
            if blog_details.page_title:
                page_title = blog_details.page_title
            else:
                page_title = blog_details.blog_title    

            context = {
                'blog_details': blog_details,
                'related_blog_post': related_blog_post,
                'user_blog_comments': user_blog_comments,
                'current_datetime': timezone.now(),
                'page_title': page_title,
            }
            return render(request, "gsmapp/pages/blog_post_details.html", context) 
        elif perma.info_type == 'product':
            product_id = perma.content
            models.ProductInfo.objects.filter(pk = product_id, status = True).update(total_view = F('total_view')+1) 
            data = models.ProductInfo.objects.filter(pk = product_id, status = True).first() 
            product_3d_view = models.ProductThreeDView.objects.filter(product_name_id = product_id)
            product_review  = models.ProductReview.objects.filter(product_name_id = product_id).first() 
            device_prices   = models.ProductPricing.objects.filter(product_name_id = product_id).order_by('device_title') 
            user_comments   = models.ProductWiseUserComment.objects.filter(product_name_id = product_id, status = True).order_by('-added_date') 

            if data.page_title:
                page_title = data.page_title
            else:
                page_title = data.product_name    

            max_price, min_price = 0,0
            if device_prices:
                max_price = device_prices[0].dollar_price+10
                min_price = device_prices[0].dollar_price-10

            similarly_price = models.ProductPricing.objects.filter(dollar_price__gte = min_price, dollar_price__lte = max_price, status = True).order_by("-product_name__total_view")[:3]
            context = {
                'data': data,
                'product_3d_view': product_3d_view,
                'product_review': product_review,
                'device_prices': device_prices,
                'user_comments': user_comments,
                'similarly_price': similarly_price,
                'page_title': page_title,
            }
            return render(request, "gsmapp/pages/product_details.html", context) 
    
    elif request.method == "POST":
        user_name     = request.POST['user_name']
        user_email    = request.POST['user_email']
        user_comment  = request.POST['user_comment']
        models.ProductWiseUserComment.objects.create(product_name_id = product_id, full_name = user_name, user_email = user_email, user_comment = user_comment)
        messages.success(request, "Your comment sent successful")
        return redirect(request.path)   


# ====================End Direct Links=========================




def product_details(request, product_id, brand_name):
    s = '/'+brand_name+'/'
    return HttpResponseRedirect(s)

def slider_product_details(request, slider_id):
    slider_product = models.SliderInfo.objects.get(pk = slider_id, status = True) 
    context = {
        'slider_product': slider_product
    }
    return render(request, "gsmapp/pages/slider_product_details.html", context) 

def blog(request):
    blog_list = models.BlogInfo.objects.filter(status = True).order_by("-added_date")
    context = {
        'blog_list': blog_list,
        'current_datetime': timezone.now()
    }
    return render(request, "gsmapp/pages/blog.html", context) 

def blog_data_ajax(request):
    blog_list = []
    if request.method == 'GET':
        myresult =  models.BlogInfo.objects.filter(status = True).order_by("-added_date")[:3]
        blog_list = []
            
        for x in myresult:
            blog_list.append([x.blog_img,x.blog_title,x.blog_slug])
            
    if request.method == 'POST':
        if 'data' in request.POST.keys():
            myresult = models.BlogInfo.objects.filter(status = True,blog_title__icontains=request.POST['data']).order_by("-added_date")[:3]

            blog_list = []
            if len(myresult)>3:
                for x in myresult[:3]:
                    blog_list.append([x.blog_img,x.blog_title,x.blog_slug])
            else:
                for x in myresult:
                    blog_list.append([x.blog_img,x.blog_title,x.blog_slug])
        

    return JsonResponse(json.dumps(blog_list,default=str),safe=False)


def blog_post_details(request, blog_slug):
    if request.method == "GET":
        blog_details = models.BlogInfo.objects.filter(blog_slug = blog_slug, status = True).first() 
        related_blog_post = models.BlogInfo.objects.filter(status = True).order_by("-added_date")[:4]
        user_blog_comments = models.BlogComments.objects.filter(status = True).order_by("-added_date")
        if blog_details.page_title:
            page_title = blog_details.page_title
        else:
            page_title = blog_details.blog_title    

        context = {
            'blog_details': blog_details,
            'related_blog_post': related_blog_post,
            'user_blog_comments': user_blog_comments,
            'current_datetime': timezone.now(),
            'page_title': page_title,
        }
        return render(request, "gsmapp/pages/blog_post_details.html", context) 
    else:
        return redirect("/") 
          
def blog_post_details_without_id(request, blog_title):
    if request.method == "GET":
        blog_details = models.BlogInfo.objects.filter(pk = request.session['blog_id'], status = True).order_by("-added_date").first()
        related_blog_post = models.BlogInfo.objects.filter(status = True).order_by("-added_date")[:4]
        user_blog_comments = models.BlogComments.objects.filter(status = True).order_by("-added_date")
        context = {
            'blog_details': blog_details,
            'related_blog_post': related_blog_post,
            'user_blog_comments': user_blog_comments,
            'current_datetime': timezone.now()
        }
        return render(request, "gsmapp/pages/blog_post_details.html", context) 
    elif request.method == "POST":
        user_name    = request.POST['user_name'].strip()
        user_email   = request.POST['user_email'].strip()
        user_comment = request.POST['user_comment'].strip()
        models.BlogComments.objects.create(blog_name_id = request.session['blog_id'], full_name = user_name, user_email = user_email, user_comment = user_comment)
        messages.success(request, "Your comment sent successful")
        return redirect("/blog/"+str(request.session['blog_id'])+"/"+str(blog_title)+"/")
    else:
        return redirect("/") 
          

def about(request):
    return render(request, "gsmapp/pages/about.html")

def faq(request):
    return render(request, "gsmapp/pages/faq.html") 

def terms(request):
    return render(request, "gsmapp/pages/terms.html")

def privacy(request):
    return render(request, "gsmapp/pages/privacy.html")

def site_map(request):
    return render(request, "gsmapp/pages/site_map.html")

def shipping_return(request):
    return render(request, "gsmapp/pages/shipping_return.html")

def international_shipping(request):
    return render(request, "gsmapp/pages/international_shipping.html")

def affiliates(request):
    return render(request, "gsmapp/pages/affiliates.html")

def secure_hopping(request):
    return render(request, "gsmapp/pages/secure_hopping.html")

def contact(request):
    return render(request, "gsmapp/pages/contact.html")

def subscribe_user_email(request):
    if request.method == "POST":
        subscribe_email = request.POST['subscribe_email']
        chk_exist = models.SubscribeEmail.objects.filter(subscribe_email = subscribe_email)
        if chk_exist:  
            messages.warning(request, "Already Subscribed")
            return redirect("/")
        else:      
            models.SubscribeEmail.objects.create(subscribe_email = subscribe_email)
            messages.success(request, "Thank you for subscribe")
            return redirect("/")

def category_product(request, cat_id, cat_name):
    print("cat_id: ", cat_id)
    request.session["cat_id"] = cat_id
    cat_name = cat_name.replace(" ","-").replace("&","-").lower()
    return redirect("/category/"+str(cat_name)+"/")

def category_wise_product(request, cat_name):
    print("cat_name: ", cat_name)
    context = {
        'cat_wise_product': models.ProductInfo.objects.filter(cat_name_id = request.session["cat_id"]).order_by("latest_device","-update_date")[:100]
    }
    return render(request, "gsmapp/pages/category_wise_product.html", context)

#-----------------Start Admin Panel------------------------------------#
def admin_login(request):
    if request.method == "GET":
        return render(request, "gsmapp/adminpanel/admin_login.html") 
    elif request.method == "POST":
        username   = request.POST["username"].strip()
        user_pass  = request.POST["user_pass"].strip() 
        user = authenticate(request, username = username, password = user_pass)
        if user: 
            login(request, user)
            return redirect("/gsm/admin-panel/dashboard/")
        else:
            return redirect("/gsm/admin-panel/login/")    
    else:
        return redirect("/")     

def admin_logout(request):
    logout(request)
    return redirect("/gsm/admin-panel/login/")     
 
def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, "gsmapp/adminpanel/admin_dashboard.html")
    else:
        return redirect("/gsm/admin-panel/logout/")    

def add_category(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "gsmapp/adminpanel/add_category.html")
        elif request.method == "POST":
            models.CategoryInfo.objects.create(cat_name = request.POST["cat_name"].strip(), ordering = request.POST["ordering"])
            messages.success(request, "Category create successful")
            return render(request, "gsmapp/adminpanel/add_category.html")
    else:
        return redirect("/gsm/admin-panel/logout/")    

def category_list(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            get_category_list = models.CategoryInfo.objects.order_by("-added_date")
            context = {
                'get_category_list': get_category_list
            }
            return render(request, "gsmapp/adminpanel/category_list.html", context) 
    else:
        return redirect("/gsm/admin-panel/logout/")  

def brand_list(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            brand_list = models.BrandInfo.objects.order_by("-added_date")
            context = {
                'brand_list': brand_list
            }
            return render(request, "gsmapp/adminpanel/brand_list.html", context) 
    else:
        return redirect("/gsm/admin-panel/logout/")  
  

def add_brand(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "gsmapp/adminpanel/add_brand.html")
        elif request.method == "POST":
            brand_name = request.POST["brand_name"]
            page_title = request.POST["page_title"]
            img_alt_tag = request.POST["img_alt_tag"]
            ordering   = request.POST["ordering"]
            is_popular = request.POST["is_popular"]
            brand_img = ""      
            if bool(request.FILES.get('brand_img', False)) == True:
                file = request.FILES['brand_img']
                brand_img = "brand/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"brand/"):
                    os.mkdir(settings.MEDIA_ROOT+"brand/")
                default_storage.save(settings.MEDIA_ROOT+"brand/"+file.name, ContentFile(file.read()))

            models.BrandInfo.objects.create(brand_name = brand_name.strip(), page_title = page_title, img_alt_tag = img_alt_tag, brand_img = brand_img, is_popular = is_popular, ordering = ordering)
            messages.success(request, "Brand create successful")
            return render(request, "gsmapp/adminpanel/add_brand.html")
    else:
        return redirect("/gsm/admin-panel/logout/")    

def edit_brand(request, brand_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            get_brand = models.BrandInfo.objects.get(pk = brand_id)
            context = {
                'get_brand': get_brand
            }
            return render(request, "gsmapp/adminpanel/edit_brand.html", context)
        elif request.method == "POST":
            brand_name = request.POST["brand_name"]
            page_title = request.POST["page_title"]
            img_alt_tag = request.POST["img_alt_tag"]
            ordering   = request.POST["ordering"]
            is_popular = request.POST["is_popular"]
            status     = request.POST["status"]
            brand_img = ""      
            if bool(request.FILES.get('brand_img', False)) == True:
                file = request.FILES['brand_img']
                brand_img = "brand/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"brand/"):
                    os.mkdir(settings.MEDIA_ROOT+"brand/")
                default_storage.save(settings.MEDIA_ROOT+"brand/"+file.name, ContentFile(file.read()))
            else:
                get_brand_img = models.BrandInfo.objects.get(pk = brand_id)
                brand_img = get_brand_img.brand_img
            
            models.BrandInfo.objects.filter(pk = brand_id).update(brand_name = brand_name.strip(), page_title = page_title, img_alt_tag = img_alt_tag, brand_img = brand_img, is_popular = is_popular, ordering = ordering, status = status)
            messages.success(request, "Brand update successful")
            return redirect("/gsm/admin/brand-list/")    
    else:
        return redirect("/gsm/admin-panel/logout/")    

def add_new_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            brand_list = models.BrandInfo.objects.filter(status = True)
            context = {
                'brand_list': brand_list
            }
            return render(request, "gsmapp/adminpanel/add_new_product.html", context)
        else:
            cat_name_id            = request.POST["cate_name"]
            display_size_top       = request.POST["display_size_top"]
            display_resolution_top = request.POST["display_resolution_top"]
            camera_photo_pixel_top = request.POST["camera_photo_pixel_top"]
            camera_video_pixel_top = request.POST["camera_video_pixel_top"]
            reviews_top = request.POST["reviews_top"]
            ram_top     = request.POST["ram_top"]
            chipset_top = request.POST["chipset_top"]
            battery_capacity_top   = request.POST["battery_capacity_top"]
            battery_technology_top = request.POST["battery_technology_top"]
            specifications_top     = request.POST["specifications_top"]
            
            overview_title = request.POST["overview_title"]
            brand_name     = request.POST["brand_name"]
            product_name   = request.POST["product_name"]
            product_model  = request.POST["product_model"]
            network_technology   = request.POST["network_technology"]
            network_2g_bands     = request.POST["network_2g_bands"]
            network_3g_bands     = request.POST["network_3g_bands"]
            network_4g_bands     = request.POST["network_4g_bands"]
            network_5g_bands     = request.POST["network_5g_bands"]
            network_speed        = request.POST["network_speed"]
            launch_announced     = request.POST["launch_announced"]
            launch_status        = request.POST["launch_status"]
            body_dimensions      = request.POST["body_dimensions"]
            body_weight          = request.POST["body_weight"]
            body_build           = request.POST["body_build"]
            body_sim             = request.POST["body_sim"]
            display_type         = request.POST["display_type"]
            display_size         = request.POST["display_size"]
            display_resolution   = request.POST["display_resolution"]
            display_protection   = request.POST["display_protection"]
            platform_os          = request.POST["platform_os"]
            platform_chipset     = request.POST["platform_chipset"]
            platform_cpu         = request.POST["platform_cpu"]
            platform_gpu         = request.POST["platform_gpu"]
            memory_card_slot     = request.POST["memory_card_slot"]
            memory_internal      = request.POST["memory_internal"]
            main_camera_type     = request.POST["main_camera_type"]
            main_cam_type_des    = request.POST["main_cam_type_des"]
            main_camera_features = request.POST["main_camera_features"]
            main_camera_video    = request.POST["main_camera_video"]
            selfie_camera_type   = request.POST["selfie_camera_type"]
            selfie_cam_type_des  = request.POST["selfie_cam_type_des"]
            selfie_camera_features = request.POST["selfie_camera_features"]
            selfie_camera_video  = request.POST["selfie_camera_video"] 
            sound_loudspeaker    = request.POST["sound_loudspeaker"] 
            sound_3_5mm_jack     = request.POST["sound_3_5mm_jack"] 
            comms_wlan           = request.POST["comms_wlan"]
            comms_bluetooth      = request.POST["comms_bluetooth"]
            comms_gps            = request.POST["comms_gps"]
            comms_nfc            = request.POST["comms_nfc"]
            comms_radio          = request.POST["comms_radio"]
            comms_usb            = request.POST["comms_usb"]
            features_sensors     = request.POST["features_sensors"]
            battery_type         = request.POST["battery_type"]
            battery_description  = request.POST["battery_description"]
            battery_charging     = request.POST["battery_charging"]
            battery_talk_time    = request.POST["battery_talk_time"]
            battery_music_play   = request.POST["battery_music_play"]
            misc_colors          = request.POST["misc_colors"]
            misc_models          = request.POST["misc_models"]
            misc_sar             = request.POST["misc_sar"]
            misc_sar_eu          = request.POST["misc_sar_eu"]
            price                = request.POST["price"]
            bd_price             = 0
            test_performance     = request.POST["test_performance"]
            test_display         = request.POST["test_display"]
            test_camera          = request.POST["test_camera"]
            test_battery_life    = request.POST["test_battery_life"]
            disclaimer           = ""
            latest_device        = request.POST["latest_device"]
            meta_title           = request.POST["meta_title"].strip()
            meta_des             = request.POST["meta_des"].strip()
            og_description       = request.POST["og_description"].strip()
            page_title           = request.POST["page_title"]
            img_alt_tag          = request.POST["img_alt_tag"]

            product_img = ""      
            if bool(request.FILES.get('product_img', False)) == True:
                file = request.FILES['product_img']
                product_img = "product_img/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"product_img/"):
                    os.mkdir(settings.MEDIA_ROOT+"product_img/")
                default_storage.save(settings.MEDIA_ROOT+"product_img/"+file.name, ContentFile(file.read()))

            models.ProductInfo.objects.create(
                cat_name_id = cat_name_id, display_size_top = display_size_top, display_resolution_top = display_resolution_top, camera_photo_pixel_top = camera_photo_pixel_top,
                camera_video_pixel_top = camera_video_pixel_top, reviews_top = reviews_top, ram_top = ram_top, chipset_top = chipset_top, meta_title = meta_title, meta_des = meta_des,
                battery_capacity_top = battery_capacity_top, battery_technology_top = battery_technology_top, specifications_top = specifications_top,

                overview_title = overview_title, brand_name_id = brand_name, product_name = product_name, product_model = product_model, network_technology = network_technology, 
                network_2g_bands = network_2g_bands, network_3g_bands = network_3g_bands, network_4g_bands = network_4g_bands, network_5g_bands = network_5g_bands,
                network_speed = network_speed, launch_announced = launch_announced, launch_status = launch_status, body_dimensions = body_dimensions, 
                body_weight = body_weight, body_build = body_build, body_sim = body_sim, display_type = display_type, display_size = display_size,
                display_resolution = display_resolution, display_protection = display_protection, platform_os = platform_os, platform_chipset = platform_chipset,
                platform_cpu = platform_cpu, platform_gpu = platform_gpu, memory_card_slot = memory_card_slot, memory_internal = memory_internal, 
                main_camera_type = main_camera_type, main_cam_type_des = main_cam_type_des, main_camera_features = main_camera_features, 
                main_camera_video = main_camera_video, selfie_camera_type = selfie_camera_type, selfie_cam_type_des = selfie_cam_type_des,
                selfie_camera_features = selfie_camera_features, selfie_camera_video = selfie_camera_video, sound_loudspeaker = sound_loudspeaker, sound_3_5mm_jack = sound_3_5mm_jack,
                comms_wlan = comms_wlan, comms_bluetooth = comms_bluetooth, comms_gps = comms_gps, comms_nfc = comms_nfc, comms_radio = comms_radio, comms_usb = comms_usb, 
                features_sensors = features_sensors, battery_type = battery_type, battery_charging = battery_charging, battery_talk_time = battery_talk_time, page_title = page_title,
                battery_description = battery_description, battery_music_play = battery_music_play, misc_colors = misc_colors, misc_models = misc_models, img_alt_tag = img_alt_tag,
                misc_sar = misc_sar, misc_sar_eu = misc_sar_eu, price = price, bd_price = bd_price, disclaimer = disclaimer, latest_device = latest_device, og_description = og_description,
                test_performance = test_performance, test_display = test_display, test_camera = test_camera, test_battery_life = test_battery_life, product_img = product_img
            )
            messages.success(request, "Product add successful")
            return render(request, "gsmapp/adminpanel/add_new_product.html") 
    else:
        return redirect("/gsm/admin-panel/logout/")      

def edit_product(request, product_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            brand_list = models.BrandInfo.objects.filter(status=True)
            data = models.ProductInfo.objects.get(pk = product_id) 
            context = {
                'data': data,
                'brand_list': brand_list,
            }
            return render(request, "gsmapp/adminpanel/edit_product.html", context)
        elif request.method == "POST":
            cat_name_id            = request.POST["cate_name"]
            display_size_top       = request.POST["display_size_top"]
            display_resolution_top = request.POST["display_resolution_top"]
            camera_photo_pixel_top = request.POST["camera_photo_pixel_top"]
            camera_video_pixel_top = request.POST["camera_video_pixel_top"]
            reviews_top = request.POST["reviews_top"]
            ram_top     = request.POST["ram_top"]
            chipset_top = request.POST["chipset_top"]
            battery_capacity_top   = request.POST["battery_capacity_top"]
            battery_technology_top = request.POST["battery_technology_top"]
            specifications_top     = request.POST["specifications_top"]
            
            overview_title = request.POST["overview_title"]
            brand_name     = request.POST["brand_name"]
            product_name   = request.POST["product_name"]
            product_model  = request.POST["product_model"]
            network_technology   = request.POST["network_technology"]
            network_2g_bands     = request.POST["network_2g_bands"]
            network_3g_bands     = request.POST["network_3g_bands"]
            network_4g_bands     = request.POST["network_4g_bands"]
            network_5g_bands     = request.POST["network_5g_bands"]
            network_speed        = request.POST["network_speed"]
            launch_announced     = request.POST["launch_announced"]
            launch_status        = request.POST["launch_status"]
            body_dimensions      = request.POST["body_dimensions"]
            body_weight          = request.POST["body_weight"]
            body_build           = request.POST["body_build"]
            body_sim             = request.POST["body_sim"]
            display_type         = request.POST["display_type"]
            display_size         = request.POST["display_size"]
            display_resolution   = request.POST["display_resolution"]
            display_protection   = request.POST["display_protection"]
            platform_os          = request.POST["platform_os"]
            platform_chipset     = request.POST["platform_chipset"]
            platform_cpu         = request.POST["platform_cpu"]
            platform_gpu         = request.POST["platform_gpu"]
            memory_card_slot     = request.POST["memory_card_slot"]
            memory_internal      = request.POST["memory_internal"]
            main_camera_type     = request.POST["main_camera_type"]
            main_cam_type_des    = request.POST["main_cam_type_des"]
            main_camera_features = request.POST["main_camera_features"]
            main_camera_video    = request.POST["main_camera_video"]
            selfie_camera_type   = request.POST["selfie_camera_type"]
            selfie_cam_type_des  = request.POST["selfie_cam_type_des"]
            selfie_camera_features = request.POST["selfie_camera_features"]
            selfie_camera_video  = request.POST["selfie_camera_video"] 
            sound_loudspeaker    = request.POST["sound_loudspeaker"] 
            sound_3_5mm_jack     = request.POST["sound_3_5mm_jack"] 
            comms_wlan           = request.POST["comms_wlan"]
            comms_bluetooth      = request.POST["comms_bluetooth"]
            comms_gps            = request.POST["comms_gps"]
            comms_nfc            = request.POST["comms_nfc"]
            comms_radio          = request.POST["comms_radio"]
            comms_usb            = request.POST["comms_usb"]
            features_sensors     = request.POST["features_sensors"]
            battery_type         = request.POST["battery_type"]
            battery_description  = request.POST["battery_description"]
            battery_charging     = request.POST["battery_charging"]
            battery_talk_time    = request.POST["battery_talk_time"]
            battery_music_play   = request.POST["battery_music_play"]
            misc_colors          = request.POST["misc_colors"]
            misc_models          = request.POST["misc_models"]
            misc_sar             = request.POST["misc_sar"]
            misc_sar_eu          = request.POST["misc_sar_eu"]
            price                = request.POST["price"]
            bd_price             = 0
            test_performance     = request.POST["test_performance"]
            test_display         = request.POST["test_display"]
            test_camera          = request.POST["test_camera"]
            test_battery_life    = request.POST["test_battery_life"]
            disclaimer           = ""
            latest_device        = request.POST["latest_device"]
            meta_title           = request.POST["meta_title"]
            meta_des             = request.POST["meta_des"]
            og_description       = request.POST["og_description"]
            page_title           = request.POST["page_title"]
            img_alt_tag          = request.POST["img_alt_tag"]

            product_img = ""      
            if bool(request.FILES.get('product_img', False)) == True:
                file = request.FILES['product_img']
                product_img = "product_img/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"product_img/"):
                    os.mkdir(settings.MEDIA_ROOT+"product_img/")
                default_storage.save(settings.MEDIA_ROOT+"product_img/"+file.name, ContentFile(file.read()))
            else:
                get_images_name = models.ProductInfo.objects.get(pk = product_id)
                product_img = get_images_name.product_img

            models.ProductInfo.objects.filter(pk = product_id).update(
                cat_name_id = cat_name_id, display_size_top = display_size_top, display_resolution_top = display_resolution_top, camera_photo_pixel_top = camera_photo_pixel_top,
                camera_video_pixel_top = camera_video_pixel_top, reviews_top = reviews_top, ram_top = ram_top, chipset_top = chipset_top, meta_title = meta_title, meta_des = meta_des,
                battery_capacity_top = battery_capacity_top, battery_technology_top = battery_technology_top, specifications_top = specifications_top,

                overview_title = overview_title, brand_name_id = brand_name, product_name = product_name, product_model = product_model, network_technology = network_technology, 
                network_2g_bands = network_2g_bands, network_3g_bands = network_3g_bands, network_4g_bands = network_4g_bands, network_5g_bands = network_5g_bands,
                network_speed = network_speed, launch_announced = launch_announced, launch_status = launch_status, body_dimensions = body_dimensions, 
                body_weight = body_weight, body_build = body_build, body_sim = body_sim, display_type = display_type, display_size = display_size,
                display_resolution = display_resolution, display_protection = display_protection, platform_os = platform_os, platform_chipset = platform_chipset,
                platform_cpu = platform_cpu, platform_gpu = platform_gpu, memory_card_slot = memory_card_slot, memory_internal = memory_internal, 
                main_camera_type = main_camera_type, main_cam_type_des = main_cam_type_des, main_camera_features = main_camera_features, page_title = page_title,
                main_camera_video = main_camera_video, selfie_camera_type = selfie_camera_type, selfie_cam_type_des = selfie_cam_type_des, img_alt_tag = img_alt_tag,
                selfie_camera_features = selfie_camera_features, selfie_camera_video = selfie_camera_video, sound_loudspeaker = sound_loudspeaker, sound_3_5mm_jack = sound_3_5mm_jack,
                comms_wlan = comms_wlan, comms_bluetooth = comms_bluetooth, comms_gps = comms_gps, comms_nfc = comms_nfc, comms_radio = comms_radio, comms_usb = comms_usb, 
                features_sensors = features_sensors, battery_type = battery_type, battery_charging = battery_charging, battery_talk_time = battery_talk_time,
                battery_description = battery_description, battery_music_play = battery_music_play, misc_colors = misc_colors, misc_models = misc_models,
                misc_sar = misc_sar, misc_sar_eu = misc_sar_eu, price = price, bd_price = bd_price, disclaimer = disclaimer, latest_device = latest_device, og_description = og_description,
                test_performance = test_performance, test_display = test_display, test_camera = test_camera, test_battery_life = test_battery_life, product_img = product_img, update_date = timezone.now()
            )
            messages.success(request, "Product update successful")
            return redirect("/gsm/admin/product-list/")  
    else:
        return redirect("/gsm/admin-panel/logout/")      

def edit_blog(request, blog_id):
    if request.user.is_authenticated:
        if request.method == "GET":
            get_blog = models.BlogInfo.objects.get(pk = blog_id)
            context = {
                'get_blog': get_blog
            }
            return render(request, "gsmapp/adminpanel/edit_blog.html", context)
        else:
            blog_title   = request.POST["blog_title"]
            short_title  = request.POST["short_title"]
            blog_details = request.POST["blog_details"]
            latest_news  = request.POST["latest_news"]
            use_slider   = request.POST["use_slider"]
            ordering     = request.POST["ordering"]
            meta_title   = request.POST["meta_title"]
            meta_des     = request.POST["meta_des"]
            og_description = request.POST["og_description"]
            source       = request.POST["source"]
            page_title   = request.POST["page_title"]
            img_alt_tag  = request.POST["img_alt_tag"]

            blog_title_slug = blog_title.lower()
            blog_title_slug = blog_title_slug.replace(",","").replace(".","").replace("#","").replace("@","").replace("!","").replace(" ","-")
            blog_title_slug = blog_title_slug.replace("*","").replace("$","").replace("%","").replace("?","").replace("&","").replace("_","-")
    
            blog_img = ""      
            if bool(request.FILES.get('blog_img', False)) == True:
                file = request.FILES['blog_img']
                blog_img = "blog/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"blog/"):
                    os.mkdir(settings.MEDIA_ROOT+"blog/")
                default_storage.save(settings.MEDIA_ROOT+"blog/"+file.name, ContentFile(file.read()))
                
                get_exist_img = models.BlogInfo.objects.get(pk = blog_id)
                if get_exist_img and get_exist_img.blog_img: 
                    try:
                        img_path = str(settings.MEDIA_ROOT)+str(get_exist_img.blog_img)
                        os.remove(img_path)
                    except:
                        pass    

                models.BlogInfo.objects.filter(pk = blog_id).update(blog_title = blog_title, short_title = short_title, blog_slug = blog_title_slug, blog_details = blog_details, latest_news = latest_news, use_slider = use_slider, ordering = ordering, blog_img = blog_img,  meta_title = meta_title, meta_des = meta_des, og_description = og_description, source = source, page_title = page_title, img_alt_tag = img_alt_tag, update_date = timezone.now())
                messages.success(request, "Blog post update successful")
                return redirect("/gsm/admin/blog-post-list/")    
            else:
                models.BlogInfo.objects.filter(pk = blog_id).update(blog_title = blog_title, short_title = short_title, blog_slug = blog_title_slug, blog_details = blog_details, latest_news = latest_news, use_slider = use_slider, ordering = ordering,  meta_title = meta_title, meta_des = meta_des,  og_description = og_description, source = source, page_title = page_title, img_alt_tag = img_alt_tag, update_date = timezone.now())
                messages.success(request, "Blog post update successful")
                return redirect("/gsm/admin/blog-post-list/")    
    else:
        return redirect("/gsm/admin-panel/logout/")      

def latest_device_list(request):
    if request.user.is_authenticated:
        get_product_list = models.ProductInfo.objects.filter(latest_device = True).order_by('-added_date')
        context = {
            'get_product_list': get_product_list
        }
        return render(request, "gsmapp/adminpanel/latest_device_list.html", context)
    else:
        return redirect("/gsm/admin-panel/logout/")      

def product_list(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            brand_list = models.BrandInfo.objects.filter(status = True)
            get_product_list = models.ProductInfo.objects.order_by('-added_date')[:50] 
            context = {
                'brand_list': brand_list,
                'get_product_list': get_product_list
            }
            return render(request, "gsmapp/adminpanel/product_list.html", context)
        elif request.method == "POST":
            brand_name   = int(request.POST['brand_name'])
            product_name = request.POST["search_product"].strip()
            
            brand_list = models.BrandInfo.objects.filter(status = True)
            get_product_list = []
            if product_name:
                get_product_list = models.ProductInfo.objects.filter(product_name__icontains = product_name).order_by('-added_date') 
            else:
                get_product_list = models.ProductInfo.objects.filter(brand_name_id = brand_name).order_by('-added_date') 
                    
            context = {
                'brand_list': brand_list,
                'get_product_list': get_product_list,
                'brand_id': brand_name
            }
            return render(request, "gsmapp/adminpanel/product_list.html", context)
    else:
        return redirect("/gsm/admin-panel/logout/")      

def latest_news_list(request):
    if request.user.is_authenticated:
        get_product_list = models.BlogInfo.objects.filter(latest_news = True).order_by('-added_date')
        context = {
            'get_product_list': get_product_list
        }
        return render(request, "gsmapp/adminpanel/latest_news_list.html", context)
    else:
        return redirect("/gsm/admin-panel/logout/")      

def blog_psot_list(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            get_blog_list = models.BlogInfo.objects.order_by('-added_date')[:50]
            cat_list      = models.CategoryInfo.objects.filter(status = True)
            context = {
                'cat_list': cat_list,
                'get_blog_list': get_blog_list
            }
            return render(request, "gsmapp/adminpanel/blog_psot_list.html", context)
        elif request.method == "POST":
            cat_id        = int(request.POST['cat_name'])
            blog_title    = request.POST['search_product']
            cat_list      = models.CategoryInfo.objects.filter(status = True)
            
            get_blog_list = []
            if blog_title:    
                get_blog_list = models.BlogInfo.objects.filter(blog_title__icontains = blog_title).order_by('-added_date')
            else:
                get_blog_list = models.BlogInfo.objects.filter(cat_name_id = cat_id).order_by('-added_date')
            
            context = {
                'cat_id': cat_id,
                'cat_list': cat_list,
                'get_blog_list': get_blog_list
            }
            return render(request, "gsmapp/adminpanel/blog_psot_list.html", context)
    else:
        return redirect("/gsm/admin-panel/logout/")      

def add_new_blog_post(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "gsmapp/adminpanel/add_new_blog_post.html")
        elif request.method == "POST":
            cat_name_id  = request.POST["cat_name"]
            blog_title   = request.POST["blog_title"]
            short_title  = request.POST["short_title"]
            blog_details = request.POST["blog_details"]
            latest_news  = request.POST["latest_news"]
            use_slider   = request.POST["use_slider"]
            ordering     = request.POST["ordering"]
            meta_title   = request.POST["meta_title"]
            meta_des     = request.POST["meta_des"]
            source       = request.POST["source"]
            page_title   = request.POST["page_title"]
            img_alt_tag  = request.POST["img_alt_tag"]

            blog_title_slug = blog_title.lower()
            blog_title_slug = blog_title_slug.replace(",","").replace(".","").replace("#","").replace("@","").replace("!","").replace(" ","-")
            blog_title_slug = blog_title_slug.replace("*","").replace("$","").replace("%","").replace("?","").replace("&","").replace("_","-")

            blog_img = ""      
            if bool(request.FILES.get('blog_img', False)) == True:
                file = request.FILES['blog_img']
                blog_img = "blog/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"blog/"):
                    os.mkdir(settings.MEDIA_ROOT+"blog/")    
                default_storage.save(settings.MEDIA_ROOT+"blog/"+file.name, ContentFile(file.read()))

            models.BlogInfo.objects.create(
                cat_name_id = cat_name_id, blog_title = blog_title, blog_slug = blog_title_slug, short_title = short_title, blog_details = blog_details, latest_news = latest_news, use_slider = use_slider, ordering = ordering, blog_img = blog_img, meta_title = meta_title, meta_des = meta_des, source = source, page_title = page_title, img_alt_tag = img_alt_tag
            )
            messages.success(request, "Blog post save successful")
            return redirect("/gsm/admin/blog-post-list/")
    else:
        return redirect("/gsm/admin-panel/logout/")   

def slider_list(request):
    if request.user.is_authenticated: 
        slider = models.BlogInfo.objects.filter(use_slider = True).order_by("-added_date")
        context = {
            'slider': slider
        }
        return render(request, "gsmapp/adminpanel/slider_list.html", context)
    else:
        return redirect("/gsm/admin-panel/logout/") 

def add_new_slider(request):
    if request.user.is_authenticated:  
        if request.method == "GET":
            return render(request, "gsmapp/adminpanel/add_new_slider.html")
        elif request.method == "POST":
            slider_name    = request.POST["slider_name"]
            slider_details = request.POST["slider_details"]
            ordering       = request.POST["ordering"]
            status         = request.POST["status"]

            slider_img = ""      
            if bool(request.FILES.get('slider_img', False)) == True:
                file = request.FILES['slider_img']
                slider_img = "slider/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"slider/"):
                    os.mkdir(settings.MEDIA_ROOT+"slider/")    
                default_storage.save(settings.MEDIA_ROOT+"slider/"+file.name, ContentFile(file.read()))
            
            models.SliderInfo.objects.create(slider_name = slider_name, slider_details = slider_details, slider_img = slider_img, ordering = ordering, status = status)
            return redirect("/gsm/admin/slider-list/")
    else:
        return redirect("/gsm/admin-panel/logout/") 

def edit_slider(request, slider_id):
    if request.user.is_authenticated: 
        if request.method == "GET":
            slider = models.SliderInfo.objects.get(pk = slider_id)
            context = {
                'slider': slider
            }
            return render(request, "gsmapp/adminpanel/edit_slider.html", context)
        elif request.method == "POST":
            slider_name    = request.POST["slider_name"]
            slider_details = request.POST["slider_details"]
            ordering       = request.POST["ordering"]
            status         = request.POST["status"]

            slider_img = ""      
            if bool(request.FILES.get('slider_img', False)) == True:
                file = request.FILES['slider_img']
                slider_img = "slider/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"slider/"):
                    os.mkdir(settings.MEDIA_ROOT+"slider/")    
                default_storage.save(settings.MEDIA_ROOT+"slider/"+file.name, ContentFile(file.read()))
            else:
                get_slider = models.SliderInfo.objects.get(pk = slider_id)
                slider_img = get_slider.slider_img

            models.SliderInfo.objects.filter(pk = slider_id).update(slider_name = slider_name, slider_details = slider_details, slider_img = slider_img, ordering = ordering, status = status)
            
            return redirect("/gsm/admin/slider-list/") 
    else:
        return redirect("/gsm/admin-panel/logout/") 

def product_3d_view(request, product_id):
    if request.user.is_authenticated: 
        if request.method == "GET":
            product    = models.ProductInfo.objects.filter(pk = product_id) 
            product_3d = models.ProductThreeDView.objects.filter(product_name_id = product_id) 
            context = {
                'product': product,
                'product_3d': product_3d
            }
            return render(request, "gsmapp/adminpanel/product_3d_view.html", context) 
        elif request.method == "POST": 
            if bool(request.FILES.get('product_3d_img', False)) == True:
                file = request.FILES['product_3d_img']
                product_3d_img = "product_3d_view/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"product_3d_view/"):
                    os.mkdir(settings.MEDIA_ROOT+"product_3d_view/")    
                default_storage.save(settings.MEDIA_ROOT+"product_3d_view/"+file.name, ContentFile(file.read()))
                models.ProductThreeDView.objects.create(product_name_id = product_id, three_d_img = product_3d_img)
                return redirect("/gsm/"+str(product_id)+"/product-3d-view/") 
            else:
                return redirect("/gsm/admin/product-list/")     
    else:
        return redirect("/gsm/admin-panel/logout/") 

def add_product_review(request, product_id):
    if request.user.is_authenticated: 
        if request.method == "GET": 
            return render(request, "gsmapp/adminpanel/add_product_review.html")  
        elif request.method == "POST":
            review_video   = request.POST["review_video"]
            review_details = request.POST["review_details"]
            models.ProductReview.objects.create(product_name_id = product_id, review_video = review_video, review_details = review_details)
            messages.success(request, "Product review add successful")
            return redirect("/gsm/admin/product-list/") 
    else:
        return redirect("/gsm/admin-panel/logout/") 

def edit_product_review(request, product_review_id):
    if request.user.is_authenticated: 
        if request.method == "GET": 
            context = {
                'product_review': models.ProductReview.objects.get(pk = product_review_id)
            }
            return render(request, "gsmapp/adminpanel/edit_product_review.html", context)  
        elif request.method == "POST":
            review_video   = request.POST["review_video"]
            review_details = request.POST["review_details"]
            models.ProductReview.objects.filter(pk = product_review_id).update(review_video = review_video, review_details = review_details)
            messages.success(request, "Product review update successful")
            return redirect("/gsm/admin/product-list/") 
    else:
        return redirect("/gsm/admin-panel/logout/") 

def product_review_details(request, product_id):
    if request.user.is_authenticated: 
        if request.method == "GET":
            product    = models.ProductInfo.objects.filter(pk = product_id) 
            product_review = models.ProductReview.objects.filter(product_name_id = product_id, status = True).first() 
            context = {
                'product_id': product_id,
                'product': product,
                'product_review': product_review
            }
            return render(request, "gsmapp/adminpanel/product_review_details.html", context)  
    else:
        return redirect("/gsm/admin-panel/logout/") 

def device_price_list(request, product_id):
    if request.user.is_authenticated: 
        if request.method == "GET":
            product    = models.ProductInfo.objects.get(pk = product_id) 
            price_list = models.ProductPricing.objects.filter(product_name_id = product_id, status = True).order_by('device_title','-added_date')
            context = {
                'product': product,
                'price_list': price_list
            }
            return render(request, "gsmapp/adminpanel/device_price_list.html", context)  
    else:
        return redirect("/gsm/admin-panel/logout/") 
    
def add_device_price(request, product_id):
    if request.user.is_authenticated: 
        if request.method == "GET":
            product    = models.ProductInfo.objects.get(pk = product_id)             
            context = { 
                'product': product, 
            }
            return render(request, "gsmapp/adminpanel/add_device_price.html", context)  
        elif request.method == "POST":   
            device_title = request.POST['device_title']
            site_link    = request.POST['site_link']
            dollar_price = request.POST['dollar_price']
            euro_price   = request.POST['euro_price']
            rupee_price  = request.POST['rupee_price']
            bd_price     = request.POST['bd_price']
            site_image = ""    
            if bool(request.FILES.get('site_image', False)) == True:
                file = request.FILES['site_image']
                site_image = "product_pricing/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"product_pricing/"):
                    os.mkdir(settings.MEDIA_ROOT+"product_pricing/")    
                default_storage.save(settings.MEDIA_ROOT+"product_pricing/"+file.name, ContentFile(file.read()))
                
            models.ProductPricing.objects.create(product_name_id = product_id, device_title = device_title, site_link = site_link, site_image = site_image, dollar_price = dollar_price, euro_price = euro_price, rupee_price = rupee_price, bd_price = bd_price)
            messages.success(request, "Device price set successful")
            return redirect("/gsm/"+ str(product_id) +"/device-price-list/") 
    else:
        return redirect("/gsm/admin-panel/logout/") 
    
def edit_device_price(request, price_id, product_id):
    if request.user.is_authenticated: 
        if request.method == "GET": 
            price = models.ProductPricing.objects.get(pk = price_id, status = True)
            context = {
                'price': price, 
            }
            return render(request, "gsmapp/adminpanel/edit_device_price.html", context)  
        elif request.method == "POST":   
            device_title = request.POST['device_title']
            site_link    = request.POST['site_link']
            dollar_price = request.POST['dollar_price']
            euro_price   = request.POST['euro_price']
            rupee_price  = request.POST['rupee_price']
            bd_price     = request.POST['bd_price']
            site_image = ""    
            if bool(request.FILES.get('site_image', False)) == True:
                file = request.FILES['site_image']
                site_image = "product_pricing/"+file.name
                if not os.path.exists(settings.MEDIA_ROOT+"product_pricing/"):
                    os.mkdir(settings.MEDIA_ROOT+"product_pricing/")    
                default_storage.save(settings.MEDIA_ROOT+"product_pricing/"+file.name, ContentFile(file.read()))
            else:
                get_product = models.ProductPricing.objects.filter(pk = price_id).first()   
                site_image  = get_product.site_image 
                
            models.ProductPricing.objects.filter(pk = price_id).update(device_title = device_title, site_link = site_link, site_image = site_image, dollar_price = dollar_price, euro_price = euro_price, rupee_price = rupee_price, bd_price = bd_price)
            messages.success(request, "Device price update successful")
            return redirect("/gsm/"+ str(product_id) +"/device-price-list/") 
    else:
        return redirect("/gsm/admin-panel/logout/") 
    
def subscribe_email_list(request):
    if request.user.is_authenticated: 
        if request.method == "GET":
            context = {
                'email_list': models.SubscribeEmail.objects.order_by("-id")
            }
            return render(request, "gsmapp/adminpanel/subscribe_email_list.html", context)  
        if request.method == "POST":
            return render(request, "gsmapp/adminpanel/subscribe_email_list.html")  
    else:
        return redirect("/gsm/admin-panel/logout/")         
    
def product_wise_comments(request):
    if request.user.is_authenticated: 
        if request.method == "GET":
            context = {
                'product_wise_comments': models.ProductWiseUserComment.objects.order_by("-id")
            }
            return render(request, "gsmapp/adminpanel/product_wise_comments.html", context)   
    else:
        return redirect("/gsm/admin-panel/logout/")
    
def delete_product_3d_view(request, p3d_id):
    if request.user.is_authenticated: 
        product_id = 0
        get_exist_img = models.ProductThreeDView.objects.get(pk = p3d_id)
        product_id = get_exist_img.product_name_id
        if get_exist_img and get_exist_img.three_d_img: 
            try:
                img_path = str(settings.MEDIA_ROOT)+str(get_exist_img.three_d_img)
                os.remove(img_path)
                get_exist_img.delete()
                return redirect("/gsm/"+str(product_id)+"/product-3d-view/") 
            except:
                get_exist_img.delete()
                return redirect("/gsm/"+str(product_id)+"/product-3d-view/")   
        else:          
            return redirect("/gsm/"+str(product_id)+"/product-3d-view/")         
    else:
        return redirect("/gsm/admin-panel/logout/")

def edit_product_3d_view(request, p3d_id):
    if request.user.is_authenticated: 
        if request.method == "GET":
            context = {
                'product_3d': models.ProductThreeDView.objects.get(pk = p3d_id)
            }
            return render(request, "gsmapp/adminpanel/edit_product_3d_view.html", context)   
        else:
            status = request.POST["status"]  
            if bool(request.FILES.get('three_d_img', False)) == True:
                file = request.FILES['three_d_img']
                three_d_img = "product_3d_view/"+file.name

                get_exist_img = models.ProductThreeDView.objects.get(pk = p3d_id)
                if get_exist_img and get_exist_img.three_d_img: 
                    try:
                        img_path = str(settings.MEDIA_ROOT)+str(get_exist_img.three_d_img)
                        os.remove(img_path)
                    except:
                        pass   
                  
                default_storage.save(settings.MEDIA_ROOT+"product_3d_view/"+file.name, ContentFile(file.read()))

                models.ProductThreeDView.objects.filter(pk = p3d_id).update(three_d_img = three_d_img, status = status) 
                return redirect("/gsm/"+str(get_exist_img.product_name_id)+"/product-3d-view/") 
            else:
                get_exist_img = models.ProductThreeDView.objects.get(pk = p3d_id)
                models.ProductThreeDView.objects.filter(pk = p3d_id).update(status = status)
                return redirect("/gsm/"+str(get_exist_img.product_name_id)+"/product-3d-view/") 
    else:
        return redirect("/gsm/admin-panel/logout/")  
      
def blog_comment_list(request):
    if request.user.is_authenticated: 
        if request.method == "GET":
            context = {
                'blog_comments': models.BlogComments.objects.order_by("-id")
            }
            return render(request, "gsmapp/adminpanel/blog_comment_list.html", context)   
    else:
        return redirect("/gsm/admin-panel/logout/")     
    
def blog_comment_active_inactive(request, blog_comment_id):
    if request.user.is_authenticated: 
        chk_status = models.BlogComments.objects.get(pk = blog_comment_id)
        if chk_status.status:
            models.BlogComments.objects.filter(pk = blog_comment_id).update(status = False)
            return redirect("/gsm/admin/blog-comment-list/")   
        else:    
            models.BlogComments.objects.filter(pk = blog_comment_id).update(status = True)
            return redirect("/gsm/admin/blog-comment-list/")         
    else:
        return redirect("/gsm/admin-panel/logout/")     
    
def product_comment_active_inactive(request, product_comment_id):
    if request.user.is_authenticated: 
        chk_status = models.ProductWiseUserComment.objects.get(pk = product_comment_id)
        if chk_status.status:
            models.ProductWiseUserComment.objects.filter(pk = product_comment_id).update(status = False)
            return redirect("/gsm/admin/product-wise-comments/")   
        else:    
            models.ProductWiseUserComment.objects.filter(pk = product_comment_id).update(status = True)
            return redirect("/gsm/admin/product-wise-comments/")         
    else:
        return redirect("/gsm/admin-panel/logout/")     

#-----------------End Admin Panel------------------------------------#    

#--------------------------Youtube video downloader--------------------#
   
# @csrf_exempt
# def youtube_videos_downloader(request):
#     try:
#         if request.method == "POST":
#             video_link = request.POST.get("video_link")
#             ydlOpts = {
#                 'noplaylist': 'true', #makes it so that if the link is in a youtube playlist it wont download the whole playlist
#                 'outtmpl': ("/home/sumon2020/mysite/static/gsmapp/youtube/youtube_video.mp4"), #output location and name
#                 'ignoreerrors': 'true', #if error move one
#                 'restrictfilenames': 'true' #gets rid of spaces in output name
#             }
#             with youtube_dl.YoutubeDL(ydlOpts)as ydl:
#                 info_dict = ydl.download([str(video_link)])
#                 result = ydl.extract_info(str(video_link), download=False)
#                 outfile = ydl.prepare_filename(result)+'.'+result['ext']
#                 video_location = "https://www.pythonanywhere.com/user/sumon2020/files"+outfile.replace("\\","/")
#             return JsonResponse({'download_location': str(video_location), 'download': 'successful'}, safe = False)
#         else:
#             return JsonResponse({'download_location': "Error", 'download': 'failed. Please use post request.'}, safe = False)
#     except:
#         return JsonResponse({'download_location': "Error", 'download': 'failed'}, safe = False)
#--------------------------Youtube video downloader--------------------#
 
     