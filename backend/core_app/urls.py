from django.urls import path, include
from rest_framework.routers import DefaultRouter


from backend.core_app.views import TransactionsViewSet, BudgetViewSet, PotsViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionsViewSet, basename='transactions')
router.register(r'budget', BudgetViewSet, basename='budget')
router.register(r'pots', PotsViewSet, basename='pots')


urlpatterns = [

    path('', include(router.urls)),  # Core app API endpoints

]