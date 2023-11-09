from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import Customer
from core_apps.business.serializers import BusinessSerializer

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




class UpdatecustomerSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "full_name",
            "email",
            "phone_number",
            "business",
        ]