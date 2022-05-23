import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shop.api.v1.serializers import MarketSerializer, VisitSerializer
from shop.models import Market, Visit


class MarketEmployeeList(ListAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def get_queryset(self):
        return Market.objects.filter(employee__phone=self.kwargs['employee__phone'])


class VisitCreate(CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
