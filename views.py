from django.shortcuts import render,redirect,get_object_or_404
from .forms import VendorRegForm1,AttachForm
from django.http import HttpResponse
from .models import Attach,VendorReg1
from Logdata import logdata
from django.contrib import messages


def vendor_registration1(request):
     if request.method == 'POST':
          form = VendorRegForm1(request.POST)
          files = request.FILES.getlist("supplierFile_attachments") # actualy image here
          if form.is_valid():
              f = form.save(commit=False)
              f.save()
              for i in files:
                   Attach.objects.create(supplier=f,supplierFile_attachments=i)
              messages.success(request,"New Supplier Created...!")
              return redirect("all_vendors")
          else:
               print(form.errors)
     else:
          form = VendorRegForm1()
          fileform = AttachForm()
          context = {
            'app_title': 'Application List',
            'username': request.user.get_full_name(),
            'isActive': request.user.is_authenticated,
            'isSuperUser': request.user.is_superuser,
            'app_title': 'Application List',
            'isForm': True,
            'isHomePage': True,
            'form': form,
            'fileform':fileform,
          }

     return render(request,'Supplier/vendor_registration1.html',context)


def vendor_detail(request, Doc_id):
    vendor = VendorReg1.objects.get(Doc_id=Doc_id)
    context = {
            'app_title': 'Application List',
            'username': request.user.get_full_name(),
            'isActive': request.user.is_authenticated,
            'isSuperUser': request.user.is_superuser,
            'app_title': 'Application List',
            'isForm': True,
            'isHomePage': True,
            'vendor': vendor,
            
          }
    return render(request, 'Supplier/vendor_detail.html', context)


def All_vendors(request):
     Vendors = VendorReg1.objects.all()
     context = {
            'app_title': 'Application List',
            'username': request.user.get_full_name(),
            'isActive': request.user.is_authenticated,
            'isSuperUser': request.user.is_superuser,
            'app_title': 'Application List',
            'isForm': True,
            'isHomePage': True,
            'Vendors': Vendors,
            
          }
     return render(request,'Supplier/Vendor_list.html',context)



def delete_kR(request):
     at = Attach.objects.get(pk=48)
     at.delete()
     return HttpResponse('delete kel')


      
def edit_supplier(request, pk):
    supplier_instance = get_object_or_404(VendorReg1, pk=pk)

    if request.method == 'POST':
        form = VendorRegForm1(request.POST, instance=supplier_instance)
        files = request.FILES.getlist("supplierFile_attachments") # actualy image here
        if form.is_valid():
              f = form.save(commit=False)
              f.save()
              for i in files:
                   Attach.objects.create(supplier=f,supplierFile_attachments=i)
        
              return redirect('all_vendors')  # Redirect to the supplier list page after successful edit
    else:
        form = VendorRegForm1(instance=supplier_instance)
        fileform = AttachForm()


        context = {
               'app_title': 'Application List',
               'username': request.user.get_full_name(),
               'isActive': request.user.is_authenticated,
               'isSuperUser': request.user.is_superuser,
               'app_title': 'Application List',
               'isForm': True,
               'isHomePage': True,
               'form': form,
               'form':form,
               'fileform':fileform,
          }

    return render(request, 'Supplier/edit_supplier.html', context)

def Delete_supplier(request, pk):
     if request.method == 'POST':
        supplier = VendorReg1.objects.get(Doc_id=pk) 
        logdata(supplier)
        supplier.delete()
        return redirect('all_vendors')
        
     




    
    

   
