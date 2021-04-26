from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product_form, name='product_insert'),
    path('<int:id>/', views.product_form,name='product_update'),
    path('delete/<int:id>/',views.product_delete, name='product_delete'),
    path('list/',views.product_list,name='product_list')
]
