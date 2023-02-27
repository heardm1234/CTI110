#Travel Expense Calculator
#26 FEB 23
#CTI-110 P2HW1-Travel
#Mallory Heard
#
print("This program calculates and displays  travel expenses")
amount = int(input("Enter Budget: "))
dest = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas?"))
hotel = int(input("Approximately, how much will you need for accomodations/hotel?"))
food = int(input("Last, how much do you need for food?"))
print("------------Travel Expenses------------")
print(f"{'Location:' : <20}" , f"{ dest: <20}")
print(f"{'Inital Budget:' : <20}" , f"{ '$'+str(float(amount)) : <20}")
print(f"{'Fuel:' : <20}" , f"{'$'+str(float(gas)) : <20}")
print(f"{'Accommodations:' : <20}" , f"{'$'+str(float(hotel)) : <20}")
print(f"{'Food:' : <20}", f"{'$'+str(float(food)) : <20}")
#Remaining Balance
remaining = amount - (gas+hotel+food)
print("---------------------------------------")
print(f"{'Remaining Balance:' : <20}" , f"{'$'+str(float(remaining)) : <20}")