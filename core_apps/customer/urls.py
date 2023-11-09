from django.urls import path

from .views import (
    CustomerListCreateView,
    CustomerRetrieveUpdateDestroyView,

)

urlpatterns = [
    path("", CustomerListCreateView.as_view(), name="customer-list-create"),
    path(
        "<uuid:id>/",
        CustomerRetrieveUpdateDestroyView.as_view(),
        name="customer-retrieve-update-destroy",
    ),
]