total_bill=int(input("enter the total bill = "))
tip = int(input("how much % of tip eg 10/20/30% = "))

tip_amt=total_bill*(tip/100)

bill_with_tip = str(total_bill+tip_amt)

print(f"total bill is {bill_with_tip} and THank YOU ")