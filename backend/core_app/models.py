from django.db import models


from backend.user import models as user_models

User = user_models.FinanceUser

CATEGORY_CHOICES = (
    ('Bills', 'Bills'),
    ('Shopping', 'Shopping'),
    ('Transportation', 'Transportation'),
    ('Lifestyle', 'Lifestyle'),
    ('Education', 'Education'),
    ('Groceries', 'Groceries'),
    ('Entertainment', 'Entertainment'),
    ('Personal Care', 'Personal Care'),
    ('General', 'General'),
    ('Dining Out', 'Dining Out'),
)

class Transactions(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )



    avatar = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=60, )
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default='expense')
    date = models.DateField(auto_now_add=True,)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2

    )
    is_recurring = models.BooleanField(default=False)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='transactions',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.type})"



class Budget(models.Model):
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES)
    maximum = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    theme = models.CharField(max_length=60, null=True, blank=True)

    transactions = models.ManyToManyField(Transactions)



    def __str__(self):
        return f"{self.category} - {self.maximum}"


class Pots(models.Model):
    name = models.CharField(max_length=60, unique=True)
    target = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    theme = models.CharField(max_length=60, null=True, blank=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='pots',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

