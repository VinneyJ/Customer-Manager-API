from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from core_apps.common.models import TimeStampedModel

User = get_user_model()

class Location(TimeStampedModel):
    country = models.CharField(
        verbose_name=_("Country"),
        max_length=50
    )
    sub_county = models.CharField(
        verbose_name=_("Sub County"),
        max_length=50
    )
    ward = models.CharField(
        verbose_name=_("Ward"),
        max_length=50
    )
    building_name = models.CharField(
        verbose_name=_("Building Name"),
        max_length=100
    )
    floor = models.CharField(
        verbose_name=_("Floor"),
        max_length=20
    )

class Business(TimeStampedModel):
    class Category(models.TextChoices):
        FINTECH = "Fintech", _("Fintech")
        LEARNING_INSTITUTION = "Learning Institution", _("Learning Institution")
        TRANSPORT = "Transport", _("Transport")
        OTHER = "Other", _("Other")

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="businesses"  # Updated related name for clarity
    )
    business_name = models.CharField(
        verbose_name=_("Business Name"),
        max_length=50
    )
    category = models.CharField(
        verbose_name=_("Category"),
        choices=Category.choices,
        default=Category.OTHER,
        max_length=20
    )
    registration_date = models.DateTimeField()
    business_age = models.PositiveIntegerField(default=0)
    
        
    def calculate_business_age(self):
        today = date.today()
        if self.business_registration_date:
            delta = today - self.business_registration_date
            return delta.days // 365
        return None

    def save(self, *args, **kwargs):
        self.business_age = self.calculate_business_age()
        super().save(*args, **kwargs)
   