
from django.db import models


class Promotion(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    description_type = models.CharField(max_length=50)
    discount_value = models.DecimalField(max_digits=15, decimal_places=2)
    min_order_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )
    max_discount_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        null=True,
        blank=True
    )
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    usage_limit = models.PositiveIntegerField(null=True, blank=True)
    used_count = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'promotions'
        ordering = ['-created_at']

    def __str__(self):
        return self.code
    

class PromotionProduct(models.Model):
    id = models.BigAutoField(primary_key=True)

    promotion = models.ForeignKey(
        Promotion,
        on_delete=models.CASCADE,
        db_column='promotion_id',
        related_name='promotion_products'
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        db_column='product_id',
        related_name='promotion_products'
    )

    class Meta:
        db_table = 'promotion_products'
        constraints = [
            models.UniqueConstraint(
                fields=['promotion', 'product'],
                name='unique_promotion_product'
            )
        ]

    def __str__(self):
        return f'{self.promotion.code} - {self.product.name}'