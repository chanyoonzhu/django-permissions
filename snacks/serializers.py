from rest_framework.serializers import ModelSerialzer
from .models import Snack

class SnackSerializer(ModelSerialzer):
    
    class Meta:
        model = Snack
        fields = ('id', 'name') # attributes of the model that we'd like to be exposed