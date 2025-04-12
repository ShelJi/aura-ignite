from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class FinanceCategory(models.Model):
    """
    Model representing a category for financial transactions.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Finance Category"
        verbose_name_plural = "Finance Categories"


class Finances(models.Model):
    """
    Model representing a financial transaction.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='finances')
    profit = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(FinanceCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='finances')

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.description}"

    class Meta:
        verbose_name = "Finance"
        verbose_name_plural = "Finances"
        ordering = ['-date']