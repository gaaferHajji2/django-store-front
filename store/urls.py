from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),

    # path('collection/<int:pk>/', views.collection_detail, name='collection-detail')

    path('collection/', views.CollectionList.as_view()),

    path('collection/<int:pk>/', views.CollectionDetail.as_view())
];