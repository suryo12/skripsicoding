# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import NodeID, Data

admin.site.register(NodeID)
admin.site.register(Data)
