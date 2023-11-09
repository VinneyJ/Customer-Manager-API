from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampedModel

from core_apps.business.models import Business

User = get_user_model()


class Customer(TimeStampedModel):
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        related_name="created_customers",
        null=True,  
        blank=True,  
    )
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        related_name="updated_customers",
        null=True,  
        blank=True,
    )
    first_name = models.CharField(verbose_name=_("first name"), max_length=50)
    last_name = models.CharField(verbose_name=_("last name"), max_length=50)
    email = models.EmailField(
        verbose_name=_("email address"), db_index=True, unique=True
    )
    phone_number = PhoneNumberField(
        verbose_name=_("phone number"), max_length=30, default="+250784123456"
    )
    country = CountryField(
        verbose_name=_("country"), default="KE", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("city"),
        max_length=180,
        default="Nairobi",
        blank=False,
        null=False,
    )
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="business")
    



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    