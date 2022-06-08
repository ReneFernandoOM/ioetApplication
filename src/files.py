import re
from typing import List

from data.constants import VALID_REGEX, WORKED_HOURS_REGEX
from utils import Employee
from errors import ExpectedError

def read_file() -> List:
    with open('src/data/employee_schedule.txt') as f:
        data = f.readlines()

    return [x.strip() for x in data]

def get_employees_from_file() -> List:
    file_data_lines = read_file()
    employees = get_employees_from_info(file_data_lines)
    return employees

def get_employees_from_info(employees_info: List) -> List:
    employees = []
    for num_line, line in enumerate(employees_info):
        re_match = re.search(VALID_REGEX, line)
        if re_match:
            employee_name, employee_worked_data = re_match.groups()
            employee_worked_hours = re.findall(WORKED_HOURS_REGEX, employee_worked_data)

            employee = Employee(employee_name)
            employee.calculate_salary(employee_worked_hours)
            employees.append(employee)
        else:
            raise ExpectedError(f'File is wrongly formatted at line: {num_line + 1}.')

    return employees