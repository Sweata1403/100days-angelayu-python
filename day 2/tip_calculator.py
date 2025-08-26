print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage of tip you would like to give? 10, 12, 15:"))
people=int(input("How many people should split the bill?"))
bill_with_tip= tip / 100 * bill + bill
print(bill_with_tip)