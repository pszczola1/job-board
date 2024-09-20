from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ListingsGetPageSerializer

from job_offers.models import JobListing

class ListingsViewset(viewsets.ModelViewSet):

    serializer_class = ListingsGetPageSerializer
    queryset = JobListing.objects.all()

    def get_queryset(self):
        queryset = JobListing.objects.all()
        
        title = self.request.query_params.get('title')
        categories = self.request.query_params.getlist('categories')
        salary = self.request.query_params.get('salary')

        if title:
            queryset = queryset.filter(title__icontains=title)  #icontains - not case sensitive
        if categories:
            for category in categories:
                queryset = queryset.filter(categories__in=category)
        if salary:
            queryset = queryset.filter(salary__gt=salary-1)

        print(queryset)
        return queryset
        