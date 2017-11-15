from rest_framework import serializers

from .models import NodeID

class NodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = NodeID
		fields = '__all__'