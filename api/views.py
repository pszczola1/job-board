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
        location = self.request.query_params.get('location')
        employment_types = self.request.query_params.getlist('employment_type')
        work_models = self.request.query_params.getlist('work_model')

        #for categories, a listing must have all categories to pass the filter
        #for employment_type and work_models, it must have only one

        if title:
            queryset = queryset.filter(title__icontains=title)  #icontains - not case sensitive

        if categories:
            for category in categories:
                queryset = queryset.filter(categories__in=category)

        if salary:
            queryset = queryset.filter(salary__gt=int(salary)-1)

        if location:
            queryset = queryset.filter(location__icontains=location)

        if employment_types: 
            filter_arr = []
            for employment_type in employment_types:
                filter_arr.append(employment_type)
            queryset = queryset.filter(employment_type__in=filter_arr) 

        if work_models:
            filter_arr = []
            for work_model in work_models:
                filter_arr.append(work_model)
            queryset = queryset.filter(work_model__in=filter_arr)

        print(queryset)
        return queryset
        