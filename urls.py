from django.contrib import admin
from django.urls import path
from Supplier import views
from Supplier.views import vendor_registration1,vendor_detail,All_vendors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_vendor/', vendor_registration1, name='create_vendor'),
    path('vendor_detail/<int:Doc_id>/', vendor_detail, name='vendor_detail'),
    path('all_vendors/',All_vendors,name='all_vendors'),
    path('vendor_avtar/<int:pk>/',All_vendors,name='vendor_avtar'),
    path('d/',views.delete_kR),
    path('edit_supplier/<int:pk>/',views.edit_supplier,name='edit_supplier'),
    path('delete_supplier/<int:pk>/',views.Delete_supplier,name='delete_supplier'),
    
   
]
