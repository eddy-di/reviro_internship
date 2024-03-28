import factory
from faker import Faker
from faker.providers import BaseProvider
from faker.providers.phone_number import Provider

from company.models import Company, Product, User

fake = Faker()


class CompanyProvider(BaseProvider):
    def schedule_weekdays_enum(self) -> int:
        return self.random_element(Company.Weekdays.values)


class KyrgyzstanPhoneProvider(Provider):
    def kg_phone_number(self):
        return f'+996{self.msisdn()[4:]}'


fake.add_provider(CompanyProvider)
fake.add_provider(KyrgyzstanPhoneProvider)


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = fake.word()
    description = fake.sentence()
    schedule_start = fake.time()
    schedule_end = fake.time()
    phone_number = fake.kg_phone_number()
    email = fake.email()
    map_link = fake.uri()
    social_media1 = fake.url()
    social_media2 = fake.url()
    social_media3 = fake.url()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = fake.word()
    description = fake.sentence()
    price = fake.pydecimal(
        left_digits=3,
        right_digits=2,
        positive=True,
        min_value=1,
        max_value=99,
    )
    discount = fake.pyint(
        min_value=0,
        max_value=100
    )
    quantity = fake.pyint()
    company = factory.SubFactory(CompanyFactory)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    username = factory.LazyAttributeSequence(
        lambda obj, count: f'{obj.first_name[:3].lower()}{obj.last_name[:3].lower()}{count}',
    )
    password = factory.django.Password('strong-test-pass')
    email = factory.LazyAttribute(lambda obj: '%s@example.com' % obj.username)
    is_superuser = False
    is_staff = False

    class Params:
        # declare a trait that adds relevant parameters for admin users
        flag_is_superuser = factory.Trait(
            is_superuser=True,
            is_staff=True,
            username=factory.Sequence(lambda n: 'admin-%d' % n),
        )

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        password = kwargs.pop('password', None)
        obj = super()._create(model_class, *args, **kwargs)
        # ensure the raw password gets set after the initial save
        obj.set_password(password)
        obj.save()
        return obj
