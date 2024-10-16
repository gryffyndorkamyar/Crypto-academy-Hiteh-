from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    is_active = models.BooleanField(default=True)
    is_sale = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Costumer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    date_ordered = models.DateField()

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    like = models.BooleanField()

    def __str__(self):
        return self.user


class CostumeUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=250, unique=True)
    first_name = models.CharField(max_length=250)

    groups = models.ManyToManyField(
        Group,
        related_name='CostumeUser_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='CostumeUser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CostumeUser, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=25, blank=True)
    address = models.CharField(max_length=250, blank=True)
    address1 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=25, blank=True)
    country = models.CharField(max_length=25, default='IRAN')
    zip = models.CharField(max_length=25, blank=True)
    first_name = models.CharField(max_length=25, blank=True)
    last_name = models.CharField(max_length=25, blank=True)
    username = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.user.first_name


class UserProfile(models.Model):
    user = models.OneToOneField(CostumeUser, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


def created_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(created_profile, sender='post.CostumeUser')
