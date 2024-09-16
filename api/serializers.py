from rest_framework import serializers
from job_offers.models import JobListing, Category

class CategoryPKToNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ListingsGetPageSerializer(serializers.ModelSerializer):
    categories = CategoryPKToNameSerializer(many=True)
    class Meta:
        model = JobListing
        fields = ('pk', 'title', 'categories', 'offered_pay')