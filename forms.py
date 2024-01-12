from django import forms
from .models import VendorReg1,Attach



class VendorRegForm1(forms.ModelForm):
    class Meta:
        model = VendorReg1
        fields = ['Doc_id', 'Nature_of_Business_Tran_with_ABL', 'Reconciliation_account', 'Vendor_Name',
                  'Vendor_name_onCheck', 'statutory_Status', 'Country', 'Region', 'street1', 'street2', 'State',
                  'street3', 'City', 'Postal_Code', 'PAN_Number', 'TAN_Number', 'GST_Number', 'GST_Register_NOT',
                  'W_Tax_Code', 'S_AND_E_Registration_Number', 'EPF_Code_Number', 'ESI_Code_Number',
                  'EC_Policy_Number', 'Registration_Number_under_Motor_Transport_Workers_Act_1961',
                  'Insurance_Policy_under_Motor_Vehicle_Act_1988', 'Email_id', 'Telephone_Number', 'Fax_Number',
                  'Mobile_Number', 'Contact_Person', 'MSME_Certificate_Number', 'BANK_NAME', 'BANK_BRANCH',
                  'BANK_CITY', 'IFSC_Code', 'ACCOUNT_NUMBER']
        

class AttachForm(forms.ModelForm):
    supplierFile_attachments = forms.FileField(
        label="File",
        widget = forms.ClearableFileInput(attrs={"multiple":True}),
    )

    class Meta:
        model = Attach
        fields = ("supplierFile_attachments",)
        