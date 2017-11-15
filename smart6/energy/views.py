from django.shortcuts import render, get_object_or_404
from .models import Customer
from .models import EnergyData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import NodeSerializer
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.views.generic.base import TemplateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils import formats, timezone

def index(request):
    all_nodes = Customer.objects.all()
    context = {
        'all_nodes':all_nodes,
    }
    return render(request, 'energy/index.html', context)

def detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    print (Customer)
    return render(request, 'energy/detail.html', {'customer': customer})


class APINodeView(APIView):
	def get(self,request):
		all_nodes = Customer.objects.all()
		serializer = NodeSerializer(all_nodes, many=True)
		return Response(serializer.data)

	def post(self,request, format=None):
		serializer = NodeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
