# Creating program in IDLE using Python
# 09 FEB 23
# CTI-110 P1HW2-Travel Expenses
# Mallory Heard
#
print("This program calculates and displays travel expenses")
budget=float(input("Enter budget:"))
dest=input("Enter your travel destination:")
gas=float(input("How much do you think you will spend on gas?"))
hotel=float(input("Approximately, how much will you need for accomodation/hotel?"))
food=float(input("Last, how much do you need for food?"))  
print("------------Travel Expenses------------")
print("Location:",dest)
print("Initial Budget:",budget)
print("\n");
print("Fuel:" ,gas)
print("Accomodations:" ,hotel)
print("Food:" ,food)
total_expense=gas+hotel+food
rem=budget-total_expense
print("\n");
print("Remaining Balance:" ,rem)