from django.test import TestCase

from shop.models import Employee, Market, Visit


class AccountModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # create user
        cls.test_employee = Employee.objects.create(name="test_employee", phone='89895')
        cls.test_market = Market.objects.create(name="test_market", employee=cls.test_employee)
        cls.test_visit = Visit.objects.create(market=cls.test_market, latitude=12.03, longitude=15.05)

    def test_employee_name_label(self):
        field_label = self.test_employee._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Имя')
