from models import Host
from rest_framework import generics
from serializers import HostSerializer
from django.shortcuts import render


class HostList(generics.ListAPIView, generics.UpdateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    model = Host


def home(request):
    return render(request, 'index.html')

