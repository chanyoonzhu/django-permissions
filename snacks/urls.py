from django.urls import path
from .views import SnackList

urlpatterns = [
    path('', SnackList.as_view(), name="snack_list")
]