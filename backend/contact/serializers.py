from rest_framework import serializers
from .models import COntact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = COntact
        fields = '__all__'