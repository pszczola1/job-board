from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ListingsGetPageSerializer

from job_offers.models import JobListing

class ListingsViewset(viewsets.ModelViewSet):

    serializer_class = ListingsGetPageSerializer
    queryset = JobListing.objects.all()

    # @action(methods=['get'], detail=False)
    # def get_page(self, request):
    #     queryset = JobListing.objects.all()
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = ListingsGetPageSerializer(queryset, many=True)
    #         return self.get_paginated_response(serializer.data)
        