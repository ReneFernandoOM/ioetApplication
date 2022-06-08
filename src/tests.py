from typing import List
import unittest

import calculator as calc
from utils import Employee
from files import get_employees_from_info, get_employees_from_file
from errors import ExpectedError

class TestCases(unittest.TestCase):

    def test_valid_data(self):
        employees = get_employees_from_info(
                ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00']
            )
        self.assertIsInstance(employees, list)

        self.assertIsInstance(employees[0], Employee)

    def test_invalid_data(self):
        with self.assertRaises(ExpectedError):
            get_employees_from_info(
                ['RENE=MOO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00']
            )
    
    def test_calc_employee_salary(self):
        employees = get_employees_from_info(
                ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00']
            )
        self.assertEqual(
            [employee.salary for employee in employees], [215]
        )

    def test_calc_employees_salaries(self):
        employees = get_employees_from_info(
                ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
                'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
            )
        self.assertEqual(
            [employee.salary for employee in employees], [215, 85]
        )

    def test_calc_employee_from_file(self):
        employees = get_employees_from_file()
        self.assertEqual(
            [employee.salary for employee in employees], [215, 85, 290, 260, 175]
        )
    
    def test_calc_run(self):
        calc.run()



if __name__ == '__main__':
    unittest.main()