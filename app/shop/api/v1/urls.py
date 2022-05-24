from django.urls import path

from shop.api.v1.views import MarketEmployeeList, VisitCreate

urlpatterns = [
    path('market/list/<str:employee__phone>/', MarketEmployeeList.as_view(), name='market-employee-list'),
    path('visit/create/<str:employee__phone>/', VisitCreate.as_view(), name='visit-create'),
]
