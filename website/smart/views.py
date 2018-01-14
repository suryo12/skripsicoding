from django.shortcuts import render, get_object_or_404
from .models import NodeID, Data
import datetime
import json

def IndexView(request):
    nodes = NodeID.objects.all()
    context = {
        'nodes' : nodes,
    }
    return render(request, 'smart/index.html', context)
    #context_object_name = 'all_albums'

    #def get_queryset(self):
    #    return Album.objects.all()


def DetailView(request, node_id):
    node = Data.objects.filter(node_id=node_id)
    context = {
        'node': node
    }
    #print(node)
    return render(request, 'smart/chart.html', context)

def LatestView(request):
    latest = Data.objects.latest('tanggal')
    context = {
        'latest' : latest,
    }
    return render(request, 'smart/detaillatest.html', context)
