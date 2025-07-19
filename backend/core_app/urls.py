from django.urls import path, include
from rest_framework.routers import DefaultRouter


from backend.core_app.views import TransactionsViewSet, BudgetViewSet, PotsViewSet, TransactionSummaryView

router = DefaultRouter()

router.register(r'budget', BudgetViewSet, basename='budget')
router.register(r'pots', PotsViewSet, basename='pots')


urlpatterns = [

    path('', include(router.urls)),  # Core app API endpoints
    path('summary/', TransactionSummaryView.as_view(), name='transaction-summary'),
    # list and create
    path('transactions/', TransactionsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='transactions-list-create'),

    # detail routes (required for GET/UPDATE/DELETE by ID)
    path('transactions/<int:pk>/', TransactionsViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'put': 'update',
        'delete': 'destroy'
    }), name='transactions-detail'),


]