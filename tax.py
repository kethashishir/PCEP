income = float(input("Enter the annual income: "))

#
# Write your code here.
#
if (income<=85528):
    tax=((18*income)/100)-556.02
else:
    taxable=income-85528
    tax=((32*taxable)/100)+14839.02

if(tax<=0):
    tax=0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
