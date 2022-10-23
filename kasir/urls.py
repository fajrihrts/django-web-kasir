from django.contrib import admin
from django.urls import path, include
from kasir.views import index, about, barang, order

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('barang', barang, name='barang'),
    path('order', order, name='order'),
    path('barang/', include('barang.urls')),
]
