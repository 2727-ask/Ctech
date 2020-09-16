from django.db import models


class Product(models.Model):
    product_id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length=50)
    product_image1 = models.ImageField(upload_to="updateSystem/images")
    product_image2 = models.ImageField(upload_to="updateSystem/images",null=True)
    product_image3 = models.ImageField(upload_to="updateSystem/images",null=True)
    product_image4 = models.ImageField(upload_to="updateSystem/images",null=True)
    product_image5 = models.ImageField(upload_to="updateSystem/images",null=True)
    product_name2 = models.CharField(max_length=50,null=True)
    product_name3 = models.CharField(max_length=50,null=True)
    product_name4 = models.CharField(max_length=50,null=True)
    product_name5 = models.CharField(max_length=50,null=True)


    def __str__(self):
        return self.product_name


class carauselImgs(models.Model):
    display_img_id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=150)
    display_img = models.ImageField(upload_to="updateSystem/images")
    def __str__(self):
        return self.display_name

class Clients(models.Model):
    Clients_id = models.AutoField(primary_key=True)
    Clients_name = models.CharField(max_length=150)
    Clients_img = models.ImageField(upload_to="updateSystem/images")
    def __str__(self):
        return self.Clients_name

class contact_us(models.Model):
    enquiry_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    cname =models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30,null=True)
    enquiry = models.CharField(max_length=500,null=True)
    phone = models.CharField(max_length=10)
    def __str__(self):
        return self.fname
