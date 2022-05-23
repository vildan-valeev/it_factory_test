from django.urls import path

from shop.api.v1.views import MarketEmployeeList, VisitCreate

urlpatterns = [
    path('market/list/<int:employee__phone>/', MarketEmployeeList.as_view()),
    path('visit/', VisitCreate.as_view()),
]
