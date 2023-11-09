from rest_framework import serializers
from .models import Location, Business

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['country', 'sub_county', 'ward', 'building_name', 'floor']

class BusinessSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = Business
        fields = ['id', 'business_name', 'category', 'registration_date', 'business_age', 'location']

    def create(self, validated_data):
        """
            Create a new Business instance
        """
        location_data = validated_data.pop('location')
        location, created = Location.objects.get_or_create(**location_data)
        business = Business.objects.create(location=location, **validated_data)
        return business

    def update(self, instance, validated_data):
        """
            Update the existing Business instance
        """
        location_data = validated_data.pop('location')
        for attr, value in location_data.items():
            setattr(instance.location, attr, value)
        instance.location.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance