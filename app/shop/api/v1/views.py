import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shop.api.v1.serializers import MarketSerializer, VisitCreateSerializer, VisitRetrieveSerializer
from shop.models import Market, Visit


class MarketEmployeeList(ListAPIView):
    serializer_class = MarketSerializer

    def get_queryset(self):
        """Фильтруем ответ по номеру телефона работника"""
        return Market.objects.filter(employee__phone=self.kwargs['employee__phone'])


class VisitCreate(CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitCreateSerializer

    def create(self, request, *args, **kwargs):
        """Добавляем условие для сохранения"""
        # TODO вынести бизнес-логику в отдельный слой для удобства тестирования
        # проверка входных данных в теле запроса
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        market = serializer.validated_data.get('market')
        phone = Market.objects.get(pk=market.id).employee.phone
        # проверка параметра запроса с данными из тела запроса
        if phone == kwargs.get('employee__phone'):
            # создание записи
            instance = serializer.save()
            # перехват сериализатора
            instance_serializer = VisitRetrieveSerializer(instance)
            print(instance_serializer.data)
            return Response(instance_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
