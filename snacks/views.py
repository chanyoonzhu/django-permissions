from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Snack
from .serializers import SnackSerializer

# Create your views here.
class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all() # when asked for snacks, return all snacks (without any filter)
    serializer_class = SnackSerializer

class SnackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
