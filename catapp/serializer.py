
from rest_framework import serializers
from catapp.models import catshop

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = catshop
        fields = '__all__'
