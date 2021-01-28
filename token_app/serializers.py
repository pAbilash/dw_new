from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from token_app.models import Test

class TestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Test
        fields = '__all__'

