hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
x=(dura+mins)//60
y=(dura+mins)%60
x=(hour+x)%24
print(x)
print(y)
print(x,':',y)