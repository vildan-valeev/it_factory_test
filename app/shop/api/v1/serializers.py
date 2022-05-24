from rest_framework import serializers

from shop.models import Market, Employee, Visit


class VisitCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ['market', 'latitude', 'longitude']


class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'visit_date', ]


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
