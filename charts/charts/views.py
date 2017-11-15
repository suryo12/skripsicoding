from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .models import EnergyData
from rest_framework import status
#from .serializer import NodeSerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.views.generic.base import TemplateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils import formats, timezone
import datetime


User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

def get_data(request, *args, **kwargs):
    data = {
        "sales":100,
        "customers":10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        gs_count = User.objects.all().count()
        label = []
        teg = []
        energies_all = EnergyData.objects.all()
        energies = EnergyData.objects.filter(tanggal__contains = datetime.date(2017, 11, 8))
        print(energies)
        for item in energies:
            if item.node_id.nama == "Suryo" :
                label.append(item.waktu)
                teg.append(item.tegangan)
        data = {
            "labels": label,
            "default": teg,
        }
        return JsonResponse(data)


#class APINodeView(APIView):
#    def get(self, request):
#        all_nodes = EnergyData.objects.all()
#        serializer = CustomerSerializer(all_nodes, many=True)
#        return Response(serializer.energydata)

#    def post(self, request, format=None):
#            serializer = CustomerSerializer(data=request.energydata)
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.energydata, status=status.HTTP_201_CREATED)
#                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
