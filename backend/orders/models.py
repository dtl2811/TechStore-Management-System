from products.models import ProductVariant
from django.db import models
from accounts.models import Customer, Address


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)

    order_code = models.CharField(
        max_length=50,
        unique=True
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        db_column='customer_id',
        related_name='orders'
    )

    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        db_column='address_id',
        related_name='orders'
    )

    order_date = models.DateTimeField()

    subtotal = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    discount_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    shipping_fee = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=30,
        default='PENDING'
    )

    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'
        ordering = ['-order_date']

    def __str__(self):
        return self.order_code


from products.models import ProductVariant


class OrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        db_column='order_id',
        related_name='items'
    )

    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.PROTECT,
        db_column='product_variant_id',
        related_name='order_items'
    )

    product_name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100)

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_items'

    def __str__(self):
        return f'{self.order.order_code} - {self.product_name}'


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        db_column='order_id',
        related_name='payment'
    )

    method = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    status = models.CharField(max_length=30, default='PENDING')
    transaction_code = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payments'

    def __str__(self):
        return f'Payment for {self.order.order_code}'


class Shipment(models.Model):
    id = models.BigAutoField(primary_key=True)

    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        db_column='order_id',
        related_name='shipment'
    )

    carrier = models.CharField(max_length=100)
    tracking_number = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    shipping_address = models.TextField()
    status = models.CharField(max_length=30, default='PENDING')
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shipments'

    def __str__(self):
        return f'Shipment for {self.order.order_code}'


from suppliers.models import Supplier


class PurchaseOrder(models.Model):
    id = models.BigAutoField(primary_key=True)

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        db_column='supplier_id',
        related_name='purchase_orders'
    )

    order_date = models.DateTimeField(auto_now_add=True)
    expected_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=30, default='PENDING')
    total_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'purchase_orders'
        ordering = ['-order_date']

    def __str__(self):
        return f'Purchase Order #{self.id}'


class PurchaseOrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)

    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        db_column='purchase_order_id',
        related_name='items'
    )

    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.PROTECT,
        db_column='product_variant_id',
        related_name='purchase_order_items'
    )

    quantity = models.PositiveIntegerField()
    unit_cost = models.DecimalField(max_digits=15, decimal_places=2)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'purchase_order_items'

    def __str__(self):
        return f'Purchase Order #{self.purchase_order_id} - Item #{self.id}'