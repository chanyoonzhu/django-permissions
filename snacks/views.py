from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Snack
from .serializers import SnackSerializer

# Create your views here.
class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all() # when asked for snacks, return all snacks (without any filter)
    serializer_class = SnackSerializer
