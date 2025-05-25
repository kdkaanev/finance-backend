from django.db import models

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
# Create your models here.
class Transactions(models.Model):


    avatar = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=60,)
    category = models.CharField(max_length=60, choices=CATEGORY_CHOICES)
    date = models.DateField()
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2

    )
