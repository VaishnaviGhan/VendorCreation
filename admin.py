from django.contrib import admin
from .models import VendorReg1,Attach,Reconciliation_acct,Region,Country,City,State
# Register your models here.
class adminVendorReg1(admin.ModelAdmin):
    list_display = ['Doc_id','Nature_of_Business_Tran_with_ABL','Reconciliation_account','Vendor_Name','Vendor_name_onCheck',
                    'statutory_Status','Country','Region']
    
admin.site.register(VendorReg1,adminVendorReg1)

class adminAttach(admin.ModelAdmin):
    list_display = ['supplier','supplierFile_attachments']
    
admin.site.register(Attach,adminAttach)



class adminReconciliation_acct(admin.ModelAdmin):
    list_display = ['Recon_id','Recon_Acc','Recon_Desc']
admin.site.register(Reconciliation_acct,adminReconciliation_acct)

class adminCountry(admin.ModelAdmin):
    list_display = ['Country_id','Country_Name']

admin.site.register(Country,adminCountry)


class adminRegion(admin.ModelAdmin):
    list_display = ['region_id','region']

admin.site.register(Region,adminRegion)


class adminState(admin.ModelAdmin):
    list_display = ['State_id','State_Name']

admin.site.register(State,adminState)

class adminCity(admin.ModelAdmin):
    list_display = ['City_id','City_Name']

admin.site.register(City,adminCity)

