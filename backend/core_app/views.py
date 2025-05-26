from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from backend.core_app.models import Transactions, Budget, Pots
from backend.core_app.serializers import TransactionsSerializer, BudgetSerializer, PotsSerializer


class TransactionsViewSet(ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']





class PotsViewSet(ModelViewSet):
    queryset = Pots.objects.all()
    serializer_class = PotsSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']



