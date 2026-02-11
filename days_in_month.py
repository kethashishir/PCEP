def is_year_leap(year):
    count=0
    if(year<1582):
        return False
    if(year%4!=0):
        count=1
    elif(year%100!=0):
        count=0
    elif(year%400!=0):
        count=1
    else:
        count=0
    if(count==0):
        return True
    else:
        return False
def days_in_month(year, month):
#
# Write your new code here.
#
    days_31=[1, 3, 5, 7, 8, 10, 12]
    days_30=[4, 6, 9, 11]
    if month in days_31:
        return 31
    elif month in days_30:
        return 30
    else:
        if is_year_leap(year)==True:
            return 29
        else:
            return 28

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")