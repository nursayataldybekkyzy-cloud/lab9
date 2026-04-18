from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('category/<int:category_id>/', views.catalog_by_category, name='catalog_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('add-category/', views.add_category, name='add_category'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-review/<int:product_id>/', views.add_review, name='add_review'),

    # AUTH
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]