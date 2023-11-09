from django import forms
from django.contrib import admin
from .models import Business, Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ["country","county", "sub_county", "ward", "building_name", "floor"]
    list_filter = ["country", "sub_county"]
    search_fields = ["country", "sub_county", "ward"]

class LocationInline(admin.StackedInline):
    model = Location
    extra = 1

class BusinessAdmin(admin.ModelAdmin):
    list_display = [
        "business_name",
        "category",
        "registration_date",
        "business_age",
        "location_country",
        "location_sub_county",
        "location_ward",
        "location_building_name",
        "location_floor"
    ]
    list_filter = ["category"]
    search_fields = ["business_name", "location__country", "location__sub_county"]

    # Use raw_id_fields to display Location as a text input with search feature
    raw_id_fields = ("location",)

    def location_country(self, obj):
        return obj.location.country

    location_country.short_description = "Country"

    def location_sub_county(self, obj):
        return obj.location.sub_county

    location_sub_county.short_description = "Sub County"

    def location_ward(self, obj):
        return obj.location.ward

    location_ward.short_description = "Ward"

    def location_building_name(self, obj):
        return obj.location.building_name

    location_building_name.short_description = "Building Name"

    def location_floor(self, obj):
        return obj.location.floor

    location_floor.short_description = "Floor"

admin.site.register(Business, BusinessAdmin)
admin.site.register(Location, LocationAdmin)