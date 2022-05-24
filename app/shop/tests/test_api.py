from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from shop.api.v1.serializers import MarketSerializer
from shop.models import Employee, Market


class MarketListTest(APITestCase):
    pass


class MainApiTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_employee = Employee.objects.create(name="test_employee", phone='89')
        cls.test_employee2 = Employee.objects.create(name="test_employee2", phone='25')
        cls.test_employee3 = Employee.objects.create(name="test_employee3", phone='55')

        cls.test_market = Market.objects.create(name="test_market", employee=cls.test_employee)
        cls.test_market2 = Market.objects.create(name="test_market2", employee=cls.test_employee2)
        cls.test_market3 = Market.objects.create(name="test_market3", employee=cls.test_employee3)

    def test_market_list(self):
        """
        Ensure we can get a  markets list.
        """
        url = reverse('market-employee-list', kwargs={"employee__phone": self.test_employee.phone})

        response = self.client.get(url, format='json')

        response_data = MarketSerializer(response.data, many=True).data
        data = MarketSerializer([self.test_market,], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response_data, data)

    def test_visit_create(self):
        """Проверяем создание Посещения"""
        url = reverse('visit-create', kwargs={"employee__phone": self.test_employee.phone})

        response = self.client.get(url, format='json')
        pass
