from django.db.models import Sum
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import permissions, request
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie


from backend.core_app.models import Transactions, Budget, Pots
from backend.core_app.serializers import TransactionsSerializer, BudgetSerializer, PotsSerializer




@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})



class TransactionsViewSet(ModelViewSet):
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        user = self.request.user
        return Transactions.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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




class TransactionSummaryView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        user = request.user
        # example logic — adapt based on your models
        transactions = Transactions.objects.filter(user=user)

        income = transactions.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        expenses = transactions.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0
        balance = income - expenses

        return Response({
            'income': income,
            'expenses': expenses,
            'balance': balance,
        })



