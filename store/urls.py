# from django.urls import path

# from rest_framework.routers import SimpleRouter

from codecs import lookup
from rest_framework.routers import DefaultRouter

from rest_framework_nested import routers

# from pprint import pprint

from . import views

router = routers.DefaultRouter()

router.register('products', views.ProductViewSet, basename='products')

router.register('collections', views.CollectionViewSet)

router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')

products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# pprint(router.urls)

# urlpatterns = [
    # path('product/', views.ProductList.as_view()),
    # path('product/<int:pk>/', views.ProductDetail.as_view()),

    # path('collection/<int:pk>/', views.collection_detail, name='collection-detail')

    # path('collection/', views.CollectionList.as_view()),

    # path('collection/<int:pk>/', views.CollectionDetail.as_view())
# ];

urlpatterns = router.urls + products_router.urls + carts_router.urls