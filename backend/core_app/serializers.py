from rest_framework import serializers

from backend.core_app.models import Transactions, Budget, Pots

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('category', 'maximum', 'theme')



class PotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pots
        fields = '__all__'