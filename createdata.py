import random
import time
from django.db import transaction
from django.core.management.base import BaseCommand
from employee.models import Employee
from employee.factories import(EmployeeFactory)
#start_time = time.time()
class Command(BaseCommand):
    
    help="Registration"
    @transaction.atomic
    def handle(self,*args, **kwargs):
        start_time = time.time()
        self.stdout.write("Deleting old Data..")
        model=Employee
        model.objects.all().delete()
        self.stdout.write("Creating new Data..")
        employee=[]
        for _ in range(10000):
            person=EmployeeFactory()
            employee.append(person)
        end_time = time.time()
        function_speed = end_time - start_time
        print('Registration complete in :',function_speed,"second")
