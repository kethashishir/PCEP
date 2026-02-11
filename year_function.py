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

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")