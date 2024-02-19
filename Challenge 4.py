MonthlyRent = int(input("Enter your monthly rent: "))
GroceryBill = int(input("Enter your grocery bill: "))
EntertainmentExpenses = int(input("Enter your Entertainment expenses: "))
TravelExpenses = int(input("Enter your Travel Expenses: "))
MiscellaneousExpenses = int(input("Enter your miscellaneous expenses: "))
MonthlyWage = 2464
Taxes = 395
Utilities = 225
Salary = MonthlyWage - MonthlyRent - GroceryBill - EntertainmentExpenses - TravelExpenses - MiscellaneousExpenses
print("Your Total Salary is {}.".format(Salary))
TotalSalary = Salary - Taxes - Utilities
print("Your total salary subtracted by your Taxes and Utility expenses is {}.".format(TotalSalary))

