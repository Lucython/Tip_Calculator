print("Welcome to the tip calculator.")
bill = input("What was the total bill? $ ")
bill_float = float(bill)
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip_int = int(tip)
people = input("How many people to split the bill? ")
people_int = int(people)
result = float(bill_float / people_int) * (1 + (tip_int/100))
result_round = round(result, 2)
print(f"Each person should pay: $ {result_round}")