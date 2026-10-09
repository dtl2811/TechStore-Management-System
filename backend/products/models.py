from django.db import models

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        db_column='parent_id',
        related_name='children',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    logo_url = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'brands'

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        db_column='category_id',
        related_name='products'
    )

    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        db_column='brand_id',
        related_name='products'
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='ACTIVE')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name  

class ProductImage(models.Model):
    id = models.BigAutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column='product_id',
        related_name='images'
    )

    image_url = models.CharField(max_length=500)
    is_main = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_images'

    def __str__(self):
        return f'{self.product.name} - Image {self.id}' 

class ProductVariant(models.Model):
    id = models.BigAutoField(primary_key=True)

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        db_column='product_id',
        related_name='variants'
    )

    sku = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    storage = models.CharField(max_length=100, blank=True, null=True)

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    stock_quantity = models.IntegerField(default=0)

    status = models.CharField(
        max_length=20,
        default='ACTIVE'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_variants'

    def __str__(self):
        return self.sku


class Inventory(models.Model):
    id = models.BigAutoField(primary_key=True)

    product_variant = models.OneToOneField(
        ProductVariant,
        on_delete=models.CASCADE,
        db_column='product_variant_id',
        related_name='inventory'
    )

    quantity = models.IntegerField(default=0)
    reserved_quantity = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'inventories'

    def __str__(self):
        return f'{self.product_variant.sku} - Stock: {self.quantity}'     


class InventoryTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)

    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.PROTECT,
        db_column='product_variant_id',
        related_name='inventory_transactions'
    )

    type = models.CharField(max_length=30)
    quantity = models.IntegerField()
    reference_id = models.BigIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inventory_transactions'
        ordering = ['-created_at']

    def __str__(self):
        return (
            f'{self.product_variant.sku} - '
            f'{self.type}: {self.quantity}'
        )