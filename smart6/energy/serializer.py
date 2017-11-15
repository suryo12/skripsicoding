from rest_framework import serializers

from .models import Customer

class NodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'