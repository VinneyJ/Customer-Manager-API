from rest_framework import serializers
from .models import Location, Business

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['country','county', 'sub_county', 'ward', 'building_name', 'floor']

    def update(self, instance, validated_data):
        """
        Update the existing Location instance.
        """
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.sub_county = validated_data.get('sub_county', instance.sub_county)
        instance.ward = validated_data.get('ward', instance.ward)
        instance.building_name = validated_data.get('building_name', instance.building_name)
        instance.floor = validated_data.get('floor', instance.floor)

        # Excluding fields from validated_data
        for field in ['created_by', 'updated_by', 'updated_at', 'created_at', 'id', 'pkid']:
            validated_data.pop(field, None)
        # Updating the Location instance
        instance.save()

        return instance

class BusinessSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    
    class Meta:
        model = Business
        fields = ['id', 'business_name', 'business_age', 'category', 'registration_date', 'location']
        read_only_fields = ['business_age'] 

    def create(self, validated_data):
        """
        Create a new Business instance along with its associated Location.
        """
        location_data = validated_data.pop('location')
        location_instance = Location.objects.create(**location_data)

        business_instance = Business.objects.create(location=location_instance, **validated_data)

        return business_instance



    def update(self, instance, validated_data):
        """
        Update the existing Business instance along with its associated Location.
        """
        instance.business_name = validated_data.get('business_name', instance.business_name)
        instance.category = validated_data.get('category', instance.category)
        instance.registration_date = validated_data.get('registration_date', instance.registration_date)

        # Excluding fields from validated_data
        for field in ['created_by', 'updated_by', 'updated_at', 'created_at', 'id', 'pkid']:
            validated_data.pop(field, None)

        # Updating the Business instance
        instance.save()

        return instance