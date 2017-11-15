import os
from django.db import models


# Create your models here.

class Customer(models.Model): #customer
    #Node_ID = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=640)
    no_telp = models.CharField(max_length=640)
    alamat = models.CharField(max_length=640)
    #data=energydata

    def __str__(self):
        return self.nama + ' - ' + self.no_telp + ' - ' + self.alamat

class EnergyData(models.Model): #energydata
    node_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tegangan = models.CharField(max_length=1000)
    energy = models.CharField(max_length=1000)
    arus = models.FloatField(null=True, blank=True, default=None)
    frekuensi = models.CharField(max_length=1000)
    total_energy = models.CharField(max_length=1000)
    tanggal = models.DateField(db_index=True, null=True, default=None)
    waktu = models.TimeField(db_index=True, null=True, default=None)
    #entered_date = datetime.datetime.strptime(date_select, '%Y-%m-%d')
    #defaultnya none


    def __str__(self):
        return str(self.tanggal) + ' - ' + str(self.waktu) + ' - ' + self.total_energy + ' - ' + str(self.arus)
