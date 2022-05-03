import factory
from factory.django import DjangoModelFactory
from .models import Employee

class EmployeeFactory(DjangoModelFactory):
    class Meta:
        model=Employee
    fullname=factory.Faker("name")
    emp_code=factory.Faker("random_number",digits=3)
    mobile=factory.Faker("msisdn")
#fake=Factory.create(fr_FR)
#fake.name()
