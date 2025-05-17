# from django.urls import path

# from rest_framework.routers import SimpleRouter

from rest_framework.routers import DefaultRouter

# from pprint import pprint

from . import views

router = DefaultRouter()

router.register('products', views.ProductViewSet)

router.register('collections', views.CollectionViewSet)

# pprint(router.urls)

# urlpatterns = [
    # path('product/', views.ProductList.as_view()),
    # path('product/<int:pk>/', views.ProductDetail.as_view()),

    # path('collection/<int:pk>/', views.collection_detail, name='collection-detail')

    # path('collection/', views.CollectionList.as_view()),

    # path('collection/<int:pk>/', views.CollectionDetail.as_view())
# ];

urlpatterns = router.urls