from django.contrib import admin

from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "pkid", "get_full_name", "email", "phone_number",
        "get_business_name", "get_business_category", "get_registration_date",
        "get_business_age", "get_location_country", "get_location_sub_county",
        "get_location_ward", "get_location_building_name", "get_location_floor",
        "created_by", "updated_by"
    ]
    list_display_links = ["pkid", "get_full_name"]
    list_filter = ["created_at", "updated_at"]
    search_fields = [
        "first_name", "last_name", "email",
        "created_by__get_full_name",
        "business__business_name",
        "business__category",
        "business__location__country",
        "business__location__sub_county",
        "business__location__ward",
        "business__location__building_name",
        "business__location__floor"
    ]

    def get_business_name(self, obj):
        return obj.business.business_name

    get_business_name.short_description = 'Business Name'

    def get_business_category(self, obj):
        return obj.business.category

    get_business_category.short_description = 'Business Category'

    def get_registration_date(self, obj):
        return obj.business.registration_date

    get_registration_date.short_description = 'Registration Date'

    def get_business_age(self, obj):
        return obj.business.business_age

    get_business_age.short_description = 'Business Age'

    def get_location_country(self, obj):
        return obj.business.location.country

    get_location_country.short_description = 'Location Country'

    def get_location_sub_county(self, obj):
        return obj.business.location.sub_county

    get_location_sub_county.short_description = 'Location Sub-county'

    def get_location_ward(self, obj):
        return obj.business.location.ward

    get_location_ward.short_description = 'Location Ward'

    def get_location_building_name(self, obj):
        return obj.business.location.building_name

    get_location_building_name.short_description = 'Location Building Name'

    def get_location_floor(self, obj):
        return obj.business.location.floor

    get_location_floor.short_description = 'Location Floor'

admin.site.register(Customer, CustomerAdmin)
