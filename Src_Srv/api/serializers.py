from rest_framework import serializers
from base.models import QueryLog

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryLog
        fields = '__all__'