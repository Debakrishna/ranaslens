from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="my_image")
    date = models.DateTimeField(auto_now_add=True )



# choices here of QueryForm



class QueryForm(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=254)
    phone_no = PhoneNumberField(null=False, blank=False)

    SERVICE_CHOICES = ( 
    ("1", "WEDDING"), 
    ("2", "CONCERT"), 
    ("3", "PORTRAIT"), 
    ("4", "PRODUCT"),   
    ) 
    service = models.CharField(max_length = 20, choices = SERVICE_CHOICES) 

    REFERENCE_CHOICE = (
    ("1", "INSTAGRAM"), 
    ("2", "GOOGLE ADS"), 
    ("3", "FACEBOOK"), 
    ("4", "TWITTER"),   
    )    
    reference = models.CharField(max_length = 20, choices = REFERENCE_CHOICE) 
    message = models.TextField()

    def __str__(self):
        return self.first_name + "'s form"