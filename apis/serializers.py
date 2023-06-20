# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import TechnoModel

# Create a model serializer
class TechnoSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = TechnoModel
		fields = ('title', 'description')
