year = int(input("Enter a year: "))

#
# Write your code here.
#
count=0
if(year<1582):
    print("Not within the Gregorian calendar period")
    exit()
if(year%4!=0):
    count=1
elif(year%100!=0):
    count=0
elif(year%400!=0):
    count=1
else:
    count=0
if(count==0):
    print("Leap year")
else:
    print("Common year")
