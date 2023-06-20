from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import TechnoSerializer
from .models import TechnoModel

# create a viewset
class TechnoViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = TechnoModel.objects.all()
	
	# specify serializer to be used
	serializer_class = TechnoSerializer
