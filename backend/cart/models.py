
from django.db import models
from accounts.models import Customer


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        db_column='customer_id',
        related_name='carts'
    )

    status = models.CharField(
        max_length=20,
        default='ACTIVE'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'carts'

    def __str__(self):
        return f'Cart #{self.id} - {self.status}'


from products.models import ProductVariant


class CartItem(models.Model):
    id = models.BigAutoField(primary_key=True)

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        db_column='cart_id',
        related_name='items'
    )

    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.PROTECT,
        db_column='product_variant_id',
        related_name='cart_items'
    )

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cart_items'
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'product_variant'],
                name='unique_cart_product_variant'
            )
        ]

    def __str__(self):
        return f'Cart {self.cart_id} - {self.product_variant.sku}'


class Wishlist(models.Model):
    id = models.BigAutoField(primary_key=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        db_column='customer_id',
        related_name='wishlists'
    )

    name = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'wishlists'

    def __str__(self):
        return f'Wishlist #{self.id}'


class WishlistItem(models.Model):
    id = models.BigAutoField(primary_key=True)

    wishlist = models.ForeignKey(
        Wishlist,
        on_delete=models.CASCADE,
        db_column='wishlist_id',
        related_name='items'
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        db_column='product_id',
        related_name='wishlist_items'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'wishlist_items'
        constraints = [
            models.UniqueConstraint(
                fields=['wishlist', 'product'],
                name='unique_wishlist_product'
            )
        ]

    def __str__(self):
        return f'Wishlist #{self.wishlist_id} - {self.product.name}'