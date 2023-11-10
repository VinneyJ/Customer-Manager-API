import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from core_apps.business.models import Business, Location
from core_apps.business.serializers import BusinessSerializer


from .models import Customer
from .pagination import CustomerPagination
from .renderers import CustomerJSONRenderer, CustomersJSONRenderer
from .serializers import CustomerSerializer



User = get_user_model()

logger = logging.getLogger(__name__)

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomerPagination  
    ordering_fields = ["created_at", "updated_at"]
    renderer_classes = [CustomersJSONRenderer]  

    def perform_create(self, serializer):
        business_data = self.request.data.get("business", {})
        business_serializer = BusinessSerializer(data=business_data)
        
        if business_serializer.is_valid():
            business_instance = business_serializer.save()
            serializer.save(created_by=self.request.user, business=business_instance)
        else:
            raise ValidationError(detail=business_serializer.errors)

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
    renderer_classes = [CustomerJSONRenderer]

    def destroy(self, request, *args, **kwargs):
      
        instance = self.get_object()

       
        business = instance.business
        business.delete()

        
        location = business.location
        location.delete()

        
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)