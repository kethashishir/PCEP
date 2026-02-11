tup=(1, ) + (1, )
tup = tup +tup
print(tup)

# Your code works because you are not 
# modifying the tuple in place. Instead,
# you are creating new tuples by concatenation:

# (1, ) + (1, ) creates (1, 1)
# tup + tup creates (1, 1, 1, 1)
# Tuples are immutable, so you cannot change their 
# contents after creation, but you can create new 
# tuples by combining existing ones. This is why 
# you can have the value 1 appear four times in the 
# final tuple. The original tuples are never changed;
# new ones are made.

def fun(x):
    global y
    y = x*x 
    return y

fun(2)
print(y)

# Even if its a global variable, it is not defined until the function is called. 
# When you call fun(2), it assigns the value 4 to the global variable y. Before that, y does not exist in the global scope.   

def fun(int=2, out=3):
    return int * out
print(fun(out=2))

# In this function definition, you have two parameters: int and out. 
# The parameter int has a default value of 2, and the parameter out has a default value of 3. 
# When you call fun(out=2), you are providing a value for the out parameter, but you are not providing 
# a value for the int parameter. Therefore, the function uses the default value of 2 for int. The calculation 
# inside the function is int * out, which evaluates to 2 * 2, resulting in 4.

def f(x=0):
    return x
print(f())
print(f(5))

# In this function definition, the parameter x has a default value of 0. 
# When you call f() without providing an argument, the function uses the default value of 0 for x, 
# so f() returns 0. When you call f(5), you are providing the value 5 for x, so f(5) returns 5.
#  The default value is only used when no argument is provided for that parameter.

# def funny(x):
#     if x%2==0:
#         return 1
#     else:
#         return  
# print(funny(funny(2))+1)

list = [i for i in range(-1, -2)]
print (list)

# The list comprehension [i for i in range(-1, -2)] generates a list of integers starting from -1 up to, but not including, -2. 
# However, since -1 is already greater than -2, the range is empty, and therefore the resulting list is empty.
#  When you print the list, it outputs [].

tup =(1, 2, 4, 8)
tup =tup[-2:-1]
print(tup)
tup=tup[-1]
print(tup)

# The expression tup[-2:-1] creates a new tuple that contains the elements from index -2 to index -1 (not including index -1). 
# In the original tuple (1, 2, 4, 8), the element at index -2 is 4, and the element at index -1 is 8.   

my_list = [ x * x for x in range(5)]

def fi(lst):
    del lst[lst[2]]
    return lst

print(fi(my_list))

# The list comprehension [x * x for x in range(5)] generates a list of squares of integers from 0 to 4, resulting in [0, 1, 4, 9, 16].
# When you call fi(my_list), it attempts to delete the element at the index specified by lst[2].
# In this case, lst[2] is 4 (the third element of the list), so it tries to delete lst[4].
# However, since the list has only 5 elements (indexed from 0 to 4), lst[4] is 16, and after deleting it, the list becomes [0,
# 1, 4, 9]. The function then returns the modified list.

z=0
y=10
x= y<z and z>y or y>z and z<y
print(x)

# The expression y<z and z>y or y>z and z<y is evaluated as follows:
# 1. y<z is evaluated first. Since y is 10 and z is 0, this evaluates to False.
# 2. z>y is evaluated next. Since z is 0 and y is
# 10, this evaluates to False.
# 3. The first part of the expression (v<z and z>y) would then evaluate to False because z>y is False.
# 4. Next, y>z is evaluated. Since y is 10 and z is 0, this evaluates to True.

foo =(1,2,3)
# foo.index(0)

# The index() method of a tuple is used to find the first occurrence of a specified value.
# In this case, you are trying to find the index of the value 0 in the tuple (1, 2, 3). Since 0 is not present in the tuple,
# the index() method raises a ValueError indicating that the value is not found in the tuple.

# try:
#     print(5/0)
#     break
# except:
#     print("Sorry, can't divide by zero.")   
# except (ValueError, ZeroDivisionError):
#     print("Too bad...") 
