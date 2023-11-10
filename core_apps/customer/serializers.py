from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from core_apps.business.serializers import BusinessSerializer, LocationSerializer
from .models import Customer
from core_apps.business.models import Location, Business

class CustomerSerializer(serializers.ModelSerializer):
    business = BusinessSerializer()

    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "business",
            "created_by",
            "updated_by",
        ]

    def get_created_by(self, obj):
        user = obj.created_by
        return self.get_user_full_name(user)

    def get_updated_by(self, obj):
        user = obj.updated_by
        if user:
            return self.get_user_full_name(user)
        return ""  

    def get_user_full_name(self, user):
        if user:
            return f"{user.first_name.title()} {user.last_name.title()}"
        return ""

    def get_full_name(self, obj):
        return f"{obj.first_name.title()} {obj.last_name.title()}"



    def create(self, validated_data):
        business_data = validated_data.pop('business', {})

        # Checking if a Business object with the same data already exists
        business, created = Business.objects.get_or_create(**business_data)

        # Using the BusinessSerializer's create or update method
        business_serializer = BusinessSerializer(instance=business, data=business_data)
        if business_serializer.is_valid():
            business_instance = business_serializer.save()
            validated_data['business'] = business_instance
        else:
            raise ValidationError(detail=business_serializer.errors)

        # Create Customer
        customer_instance = Customer.objects.create(
            created_by=self.context['request'].user,
            **validated_data
        )

        return customer_instance



    def update(self, instance, validated_data):
    
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)


        business_data = validated_data.pop('business', {})
        location_data = business_data.pop('location', None)

        # Update the Location instance if location_data is provided
        if location_data:
            location_serializer = LocationSerializer(instance=instance.business.location, data=location_data, partial=True)
            if location_serializer.is_valid():
                location_serializer.save()
            else:
                raise ValidationError(detail=location_serializer.errors)

        # Update the Business instance
        business_serializer = BusinessSerializer(instance=instance.business, data=business_data, partial=True)
        if business_serializer.is_valid():
            business_serializer.save()
        else:
            raise ValidationError(detail=business_serializer.errors)

        # Update the Customer instance
        instance.save()

        return instance