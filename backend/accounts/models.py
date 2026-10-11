from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    status = models.CharField(max_length=20, default='ACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'roles'

    def __str__(self):
        return self.name


class UserRole(models.Model):
    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='user_roles'
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        db_column='role_id',
        related_name='user_roles'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_roles'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'role'],
                name='unique_user_role'
            )
        ]

    def __str__(self):
        return f'{self.user.username} - {self.role.name}'


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='customer'
    )

    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.full_name


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        db_column='customer_id',
        related_name='addresses'
    )

    receiver_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'addresses'

    def __str__(self):
        return f'{self.receiver_name} - {self.address_line}'


class Review(models.Model):
    id = models.BigAutoField(primary_key=True)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        db_column='customer_id',
        related_name='reviews'
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        db_column='product_id',
        related_name='reviews'
    )

    order_item = models.ForeignKey(
        'orders.OrderItem',
        on_delete=models.CASCADE,
        db_column='order_item_id',
        related_name='reviews'
    )

    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=30, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.customer.full_name} - {self.product.name}'