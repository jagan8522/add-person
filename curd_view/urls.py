from django.urls import path

from . import views

urlpatterns = [
    path('',views.product_view),
    path('delete/<int:id>/', views.delete_product, name='product_delete'),
    path('update/<int:id>/', views.update_product, name='edit_product')
]