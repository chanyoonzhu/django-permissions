from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Snack
from .serializers import SnackSerializer
from .permissions import IsPurchaserOrReadOnly

# Create your views here.
class SnackList(ListCreateAPIView):
    queryset = Snack.objects.all() # when asked for snacks, return all snacks (without any filter)
    serializer_class = SnackSerializer
    permission_classes = (IsPurchaserOrReadOnly, ) # a tuple with a single item needs a comma

class SnackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = (IsPurchaserOrReadOnly, ) # a tuple with a single item needs a comma

