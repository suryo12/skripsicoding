from rest_framework import serializers

from .models import EnergyData, Customer

class NodeIDSerializer(serializers.ModelSerializer):
	class Meta:
		model = EnergyData
		fields = '__all__'