import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from core_apps.business.models import Business, Location


from .models import Customer
from .pagination import CustomerPagination
from .renderers import CustomerJSONRenderer, CustomersJSONRenderer
from .serializers import CustomerSerializer



User = get_user_model()

logger = logging.getLogger(__name__)

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomerPagination  # You may have a custom pagination class
    ordering_fields = ["created_at", "updated_at"]
    renderer_classes = [CustomersJSONRenderer]  # Your custom renderer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    #permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
    renderer_classes = [CustomerJSONRenderer]

    def perform_update(self, serializer):
        instance = serializer.save(updated_by=self.request.user)
        
        
        try:
            # Check if the request contains data for the related Business
            business_data = self.request.data.get("business")
            if business_data:
                business, created = Business.objects.get_or_create(id=business_data.get("id"))
                business.business_name = business_data.get("business_name")
                business.category = business_data.get("category")
                business.registration_date = business_data.get("registration_date")
                business.save()
                
                # Check if the request contains data for the related Location
                location_data = business_data.get("location")
                if location_data:
                    location, created = Location.objects.get_or_create(id=location_data.get("id"))
                    location.country = location_data.get("country")
                    location.sub_county = location_data.get("sub_county")
                    location.ward = location_data.get("ward")
                    location.building_name = location_data.get("building_name")
                    location.floor = location_data.get("floor")
                    location.save()
        except Exception as e:
            raise ValidationError(detail={'error': 'Failed to update related Business and Location'}) from e
        
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(instance)

        return Response(serializer.data)
