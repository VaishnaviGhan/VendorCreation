from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from multiupload.fields import MultiFileField
import os

# Create your models here.
class Reconciliation_acct(models.Model):
    Recon_id = models.AutoField(primary_key=True)
    Recon_Acc = models.IntegerField()
    Recon_Desc = models.CharField(max_length=70)
    def __str__(self):
        return self.Recon_Desc

class Country(models.Model):
    Country_id = models.AutoField(primary_key=True)
    Country_Name = models.CharField(max_length=70)

    def __str__(self):
        return self.Country_Name


class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region = models.CharField(max_length=70)
    
    def __str__(self):
        return self.region


class State(models.Model):
    State_id = models.AutoField(primary_key=True)
    State_Name = models.CharField(max_length=70)


    def __str__(self):
        return self.State_Name


class City(models.Model):
    City_id = models.AutoField(primary_key=True)
    City_Name = models.CharField(max_length=70)

    def __str__(self):
        return self.City_Name



class VendorReg1(models.Model):
    Doc_id = models.AutoField(primary_key=True)
    Nature_of_Business_Tran_with_ABL = models.CharField(max_length=70,default='Material Supply')
    Reconciliation_account = models.ForeignKey(Reconciliation_acct,on_delete=models.CASCADE,null=True,blank=True)
    Vendor_Name = models.CharField(max_length=70,null=True,blank=True)
    Vendor_name_onCheck = models.CharField(max_length=70,null=True,blank=True)
    statutory_Status = models.CharField(max_length=70,null=True,blank=True)
    Country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    Region = models.ForeignKey(Region,on_delete=models.CASCADE,null=True,blank=True)
    street1 = models.CharField(max_length=70,null=True,blank=True)
    street2 = models.CharField(max_length=70,null=True,blank=True)
    State = models.ForeignKey(State,on_delete=models.CASCADE,null=True,blank=True)
    street3 = models.CharField(max_length=70,null=True,blank=True)
    City = models.ForeignKey(City,on_delete=models.CASCADE,null=True,blank=True)
    Postal_Code = models.IntegerField(
        validators=[
            MinValueValidator(100000, message="Postal code must be a 6-digit number."),
            MaxValueValidator(999999, message="Postal code must be a 6-digit number.")
        ],null=True,blank=True
    )
    PAN_Number = models.IntegerField(
        validators=[
            MinValueValidator(1000000000, message="PAN_Number must be a 10-digit number."),
            MaxValueValidator(9999999999, message="PAN_Number must be a 10-digit number.")
        ],null=True,blank=True
    )

    TAN_Number = models.IntegerField(
        validators=[
            MinValueValidator(1000000000, message="PAN_Number must be a 10-digit number."),
            MaxValueValidator(9999999999, message="PAN_Number must be a 10-digit number.")
        ],null=True,blank=True
    )
    GST_Number = models.IntegerField(
        validators=[
            MinValueValidator(100000000000000, message="PAN_Number must be a 15-digit number."),
            MaxValueValidator(999999999999999, message="PAN_Number must be a 15-digit number.")
        ],null=True,blank=True
    )
    GST_Register_NOT = models.CharField(max_length=70,null=True,blank=True)
    W_Tax_Code = models.CharField(max_length=70,null=True,blank=True)
    S_AND_E_Registration_Number = models.CharField(max_length=70,null=True,blank=True)
    EPF_Code_Number = models.IntegerField(null=True,blank=True)
    ESI_Code_Number = models.IntegerField(null=True,blank=True)
    EC_Policy_Number = models.IntegerField(null=True,blank=True)
    Registration_Number_under_Motor_Transport_Workers_Act_1961 = models.IntegerField(null=True,blank=True)
    Insurance_Policy_under_Motor_Vehicle_Act_1988 = models.IntegerField(null=True,blank=True)
    Email_id = models.EmailField(null=True,blank=True)
    Telephone_Number = models.CharField(max_length=70,null=True,blank=True)
    Fax_Number = models.CharField(max_length=70,null=True,blank=True)
    Mobile_Number = models.CharField(max_length=70,null=True,blank=True)
    Contact_Person = models.CharField(max_length=70,null=True,blank=True)
    MSME_Certificate_Number = models.CharField(max_length=70,null=True,blank=True)
    BANK_NAME = models.CharField(max_length=70,null=True,blank=True)
    BANK_BRANCH = models.CharField(max_length=70,null=True,blank=True)
    BANK_CITY = models.CharField(max_length=70,null=True,blank=True)
    IFSC_Code = models.IntegerField(
        validators=[
            MinValueValidator(10000000000, message="IFSC_Code must be a 11-digit number."),
            MaxValueValidator(99999999999, message="IFSC_Code must be a 11-digit number.")
        ],null=True,blank=True
    )
    ACCOUNT_NUMBER = models.IntegerField(
        validators=[
            MinValueValidator(100000000000000000, message="Account Number must be a 11-digit number."),
            MaxValueValidator(999999999999999999, message="Account Number must be a 11-digit number.")
        ],null=True,blank=True
    )


    def __str__(self):
        return str(self.Doc_id)
   



class Attach(models.Model):
    supplier = models.ForeignKey(VendorReg1,on_delete=models.CASCADE)
    supplierFile_attachments = models.FileField(upload_to='Supplier_Documentations/')
   


