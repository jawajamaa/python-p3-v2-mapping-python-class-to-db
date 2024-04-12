#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)
# prints: Department 1: Payroll, Buiding A, 5th Floor

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  
# prints: Department 2: Human Resources, Building C, East Wing

accounting = Department.create("Accounting", "Building A, 4th Floor")
print(accounting)

hr.name = 'HR'
hr.location = 'Building F, 10th Floor'
hr.update()
print(hr)

print("Delete Payroll")
payroll.delete()
print(payroll)

# payroll = Department("Payroll", "Building A, 5th Floor") 
# print(payroll) """ prints: Department None: Payroll, Buiding A, 5th Floor"""

# payroll.save() """ persist to db, assign object id attribute """
# print(payroll) """ prints: Department 1: Payroll, Buiding A, 5th Floor"""

# hr = Department("Human Resources", "Building C, East Wing")
# print(hr) """ prints: Department None: Human Resources, Building C, East Wing"""


# hr.save()""" persist to db, assign object id attribute """
# print(hr)""" prints: Department 2: Human Resources, Building C, East Wing"""


ipdb.set_trace()
