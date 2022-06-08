# ioetApplication
Ioet - coding exercise.

## Coding exercise

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

|Monday - Friday|Dollar/Hour|
|--------------|-------|
|00:01 - 09:00 | 25 USD|
|09:01 - 18:00 | 15 USD|
|18:01 - 00:00 | 20 USD|

|Saturday and Sunday|Dollar/Hour|
|--------------|-------|
|00:01 - 09:00 | 30 USD|
|09:01 - 18:00 | 20 USD|
|18:01 - 00:00 | 25 USD|

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

|Code|Day|
|----|---|
|MO| Monday|
|TU| Tuesday|
|WE| Wednesday|
|TH| Thursday|
|FR| Friday|
|SA| Saturday|
|SU| Sunday|

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

For example:

Case 1:

INPUT

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

## Solution
In order to solve the exercise, I had to first figure out how would I check if the hours are inside a given interval. After solving that problem, I encounter another similar problem: what happens if a person works between two different payment ranges? After solving this, it was much easier, since all the heavy lifting was already done.

## Run script
Simply use `python main.py`

To try different data, just modify the file `employee_schedule.txt` under src/data

## Run tests
Simply use `python src/tests.py`
