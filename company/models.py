from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class Company(models.Model):
    class Weekdays(models.IntegerChoices):
        ALL_WEEK_DAYS = 0, 'All Week Days'
        MONDAY = 1, 'Monday'
        TUESDAY = 2, 'Tuesday'
        WEDNESDAY = 3, 'Wednesday'
        THURSDAY = 4, 'Thursday'
        FRIDAY = 5, 'Friday'
        SATURDAY = 6, 'Saturday'
        SUNDAY = 7, 'Sunday'

    phone_regex = RegexValidator(
        regex=r'^\+\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )

    name = models.CharField(max_length=32)
    description = models.TextField(max_length=1000)
    schedule_start = models.TimeField(null=True, blank=True)
    schedule_end = models.TimeField(null=True, blank=True)
    schedule_weekdays = models.IntegerField(
        default=Weekdays.ALL_WEEK_DAYS,
        choices=Weekdays.choices,
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
    )
    email = models.EmailField(null=True, blank=True)
    map_link = models.CharField(max_length=2000, null=True, blank=True)
    social_media1 = models.URLField(null=True, blank=True)
    social_media2 = models.URLField(null=True, blank=True)
    social_media3 = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'companies'


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(
        default=0.00,
        null=True,
        blank=True,
        max_digits=10,
        decimal_places=2,
    )
    discount = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    quantity = models.IntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


def upload_to(instance, filename):
    return f'avatars/{filename}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {'refresh': str(refresh), 'access': str(refresh.access_token)}
