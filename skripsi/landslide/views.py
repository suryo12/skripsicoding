from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import NodeID, Data
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
import datetime
import json


def index(request):
    all_nodes = NodeID.objects.all()
    context = {
        'all_nodes':all_nodes,
    }
    return render(request, 'landslide/index.html', context)

def get_data_show(request):
    data = Data.objects.filter(node_id_id = 1)
    return render(request, 'landslide/tanggal.html', {'data' : data})

#def detail(request, nodeid_id):
#    nodeids = get_object_or_404(Data, id=data_tanggal)
#    return render(request, 'landslide/detail.html', {'nodeid': nodeids})

#def detail(request, nodeid_id):
    #nodeid = get_object_or_404(NodeID, id=nodeid_id)
    # TODO: ambil dari db
    #datax = [];
    #datax = Data.objects.filter(tanggal__contains=datetime.date(2017, 11, 13))
    #datay = [];
    #def get(self, request, format=None):
    #label = []
    #teg = []
    #for item in Data.objects.filter(tanggal__contains=datetime.date(2017, 11, 11)):
    #    label.append(item.waktu)
    #    teg.append(item.tegangan)
    #    data = {
    #        "labels": label,
    #        "default": teg,
    #    }
        #return render(request, 'landslide/detail.html', {'data': data})
    #    return JsonResponse(data)
        #return JsonResponse(data)
        #waktu = item.waktu

        #itemhasil = {
        #    "x": item.waktu.isoformat(),
        #    "y": item.tegangan,
        #}
        #datax.append(itemhasil)
        #teg.append(item.tegangan)
        # #return JsonResponse(datax, safe = False)
        #return render(request, 'landslide/detail.html', {'nodeid': nodeid, "datax": json.dumps(datax)})
    # TODO: muat data db ke variabel data



    #nodeid = get_object_or_404(NodeID, id=nodeid_id)
    #return render(request, 'landslide/detail.html', {'nodeid': nodeid})

def chart(request, data_id):
    datatanggal = Data.objects.filter(tanggal__contains = datetime.date(2017, 11, 13))
    return JsonResponse(datatanggal)

def detail(request, nodeid_id):
    nodeid = get_object_or_404(NodeID, id=nodeid_id)
    return render(request, 'landslide/detail.html', {'nodeid': nodeid})

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
            if item.node_id.nama == "Agung" :
                label.append(item.waktu)
                teg.append(item.tegangan)
        data = {
            "labels": label,
            "default": teg,
        }
        return JsonResponse(data)


class APINodeView(APIView):
	def get(self,request):
		all_nodes = NodeID.objects.all()
		serializer = NodeSerializer(all_nodes, many=True)
		return Response(serializer.data)

	def post(self,request, format=None):
		serializer = NodeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)