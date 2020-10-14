from django.urls import path, include
from gsmapp import views 
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name="home_page"), 
    path('search_data_ajax/', views.search_data_ajax, name="search_data_ajax"), 
    path('blog_data_ajax/', views.blog_data_ajax, name="blog_data_ajax"), 
    path('compare_product/', views.compare_product, name="compare_product"),
    
    path('gsm/brand/', views.brand, name="brand"), 
    path('gsm/blog/', views.blog, name="blog"), 
    path('gsm/about/', views.about, name="about"),
    path('gsm/faq/', views.faq, name="faq"),
    path('gsm/terms/', views.terms, name="terms"),
    path('gsm/privacy/', views.privacy, name="privacy"),
    path('gsm/site_map/', views.site_map, name="site_map"),
    path('gsm/shipping_return/', views.shipping_return, name="shipping_return"),
    path('gsm/secure_hopping/', views.secure_hopping, name="secure_hopping"),
    path('gsm/international_shipping/', views.international_shipping, name="international_shipping"),
    path('gsm/affiliates/', views.affiliates, name="affiliates"),
    path('gsm/contact/', views.contact, name="contact"),
    path('gsm/brand/<str:brand_name>/', views.brand_wise_product, name="brand_wise_product"), 
    # ======================direct links==========================
    path('<str:name>/', views.direct_details, name="direct_details"), 
    
    # ===================end direct links=========================
    path('<int:product_id>/<str:brand_name>/', views.product_details, name="product_details"), 
    # path('<str:blog_slug>/', views.blog_post_details, name="blog_post_details"),    
    # path('blog/<str:blog_title>/', views.blog_post_details_without_id, name="blog_post_details_without_id"),    
    path('gsm/<int:product_id>/edit-product/', views.edit_product, name="edit_product"),    
    path('gsm/<int:blog_id>/edit-blog/', views.edit_blog, name="edit_blog"),    
    path('gsm/<int:slider_id>/slider-product-details/', views.slider_product_details, name="slider_product_details"),    
    path('gsm/<int:product_id>/product-3d-view/', views.product_3d_view, name="product_3d_view"),    
    path('gsm/<int:product_id>/add-product-review/', views.add_product_review, name="add_product_review"),    
    path('gsm/<int:product_review_id>/edit-product-review/', views.edit_product_review, name="edit_product_review"),    
    path('gsm/<int:product_id>/product-review-details/', views.product_review_details, name="product_review_details"),    
    path('gsm/<int:brand_id>/edit-brand/', views.edit_brand, name="edit_brand"),    
    path('gsm/<int:product_id>/device-price-list/', views.device_price_list, name="device_price_list"),    
    path('gsm/<int:product_id>/add-device-price/', views.add_device_price, name="add_device_price"),    
    path('gsm/<int:price_id>/<int:product_id>/edit-device-price/', views.edit_device_price, name="edit_device_price"),       
    # path('tools/youtube-videos-downloader/', views.youtube_videos_downloader, name="youtube_videos_downloader"),     
    path('gsm/subscribe-user-email/', views.subscribe_user_email, name="subscribe_user_email"),  
    path('category/<int:cat_id>/<str:cat_name>/', views.category_product, name="category_product"),  
    path('category/<str:cat_name>/', views.category_wise_product, name="category_wise_product"),  
    path('ajax/get-next-product/', views.get_next_product, name="get_next_product"),  
    path('sitemap.xml', views.sitemap, name="sitemap"), 
        
        
    #------------Website Admin Panel--------------#
    path('gsm/admin-panel/login/', views.admin_login, name="admin_login"), 
    path('gsm/admin-panel/logout/', views.admin_logout, name="admin_logout"), 
    path('gsm/admin-panel/dashboard/', views.admin_dashboard, name="admin_dashboard"), 
    path('gsm/admin/add-new-product/', views.add_new_product, name="add_new_product"), 
    path('gsm/admin/product-list/', views.product_list, name="product_list"), 
    path('gsm/admin/latest-device-list/', views.latest_device_list, name="latest_device_list"), 
    path('gsm/admin/add-new-blog-post/', views.add_new_blog_post, name="add_new_blog_post"), 
    path('gsm/admin/latest-news-list/', views.latest_news_list, name="latest_news_list"), 
    path('gsm/admin/blog-post-list/', views.blog_psot_list, name="blog_psot_list"), 
    path('gsm/admin/blog-comment-list/', views.blog_comment_list, name="blog_comment_list"),    
    path('gsm/admin/add-category/', views.add_category, name="add_category"),  
    path('gsm/admin/category-list/', views.category_list, name="category_list"),
    path('gsm/admin/add-brand/', views.add_brand, name="add_brand"),
    path('gsm/admin/brand-list/', views.brand_list, name="brand_list"),
    path('gsm/admin/slider-list/', views.slider_list, name="slider_list"),
    path('gsm/admin/add-new-slider/', views.add_new_slider, name="add_new_slider"),
    path('gsm/admin/<int:slider_id>/edit-slider/', views.edit_slider, name="edit_slider"),
    path('gsm/admin/subscribe-email-list/', views.subscribe_email_list, name="subscribe_email_list"),  
    path('gsm/<int:blog_comment_id>/blog-comment-active-inactive/', views.blog_comment_active_inactive, name="blog_comment_active_inactive"), 
    path('gsm/<int:product_comment_id>/product-comment-active-inactive/', views.product_comment_active_inactive, name="product_comment_active_inactive"), 
    path('gsm/admin/product-wise-comments/', views.product_wise_comments, name="product_wise_comments"), 
    path('gsm/admin/<int:p3d_id>/edit-product-3d-view/', views.edit_product_3d_view, name="edit_product_3d_view"),
    path('gsm/admin/<int:p3d_id>/delete-product-3d-view/', views.delete_product_3d_view, name="delete_product_3d_view"),
    #------------End Website Admin Panel--------------#
]
