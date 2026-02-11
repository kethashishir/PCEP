c0= int(input("Enter an integer:"))
c=0
if c0<=0:
    print("The input must be a positive integer.")
    exit()
print(c0)
while (c0!=1):
    if c0%2==0:
        c0/=2
    else:
        c0=3*c0+1
    print(round(c0))
    c+=1
print(c)
    