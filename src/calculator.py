import os
from typing import Union

from files import get_employees_from_file, get_employees_from_info


def run(employees_info: Union[str, bool]=False):
    
    if employees_info:
        employees = get_employees_from_info(employees_info)
    else: 
        employees = get_employees_from_file()
        
    for employee in employees:
        print(f'The amount to pay {employee.name} is: {employee.salary} USD')

