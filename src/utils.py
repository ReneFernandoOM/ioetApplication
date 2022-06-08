from datetime import datetime
from typing import Tuple
from data.constants import PAYMENT_INFO, WEEKEND, WEEKEND_BONUS

class Employee:
    
    def __init__(self, name):
        self.name = name
        self.salary = 0

    @staticmethod
    def get_time_range_from_string(time_range_string:str) -> Tuple:
        init_range, end_range = time_range_string.split('-')
        return (datetime.strptime(init_range, '%H:%M').time(),
                datetime.strptime(end_range, '%H:%M').time())

    def calculate_salary(self, week_worked_hours:str):
        payment_time_range = {k: self.get_time_range_from_string(k) for k, v in PAYMENT_INFO.items()}
        for work_day in week_worked_hours:
            day, worked_hours = work_day
            init_work_hour, end_work_hour = self.get_time_range_from_string(worked_hours)
            hours_worked = end_work_hour.hour - init_work_hour.hour

            bonus = 0
            if day in WEEKEND:
                bonus = WEEKEND_BONUS

            for time_range_string, time_range in payment_time_range.items():
                if init_work_hour >= time_range[0] and end_work_hour <= time_range[1]:
                    self.salary += (PAYMENT_INFO[time_range_string] + bonus) * hours_worked

                elif init_work_hour > time_range[0] and init_work_hour < time_range[1]:
                    hours_worked_in_range = time_range[1].hour - init_work_hour.hour

                    self.salary += (PAYMENT_INFO[time_range_string] + bonus) * (hours_worked_in_range)
                    hours_worked -= hours_worked_in_range

                elif end_work_hour > time_range[0] and end_work_hour < time_range[1]:
                    self.salary += (PAYMENT_INFO[time_range_string] + bonus) * hours_worked
                


            



    

