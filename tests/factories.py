import factory
from faker import Faker
from faker.providers import BaseProvider

from company.models import Company, Product

fake = Faker()


class CompanyProvider(BaseProvider):
    def schedule_weekdays_enum(self) -> int:
        return self.random_element(Company.Weekdays.values)


fake.add_provider(CompanyProvider)


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = fake.word()
    description = fake.sentence()
    schedule_start = fake.time()
    schedule_end = fake.time()
    # schedule_weekdays = fake.schedule_weekdays_enum()
    phone_number = fake.phone_number()
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
