#to shift value from one variable to the other using a temporary variable
a=int(input("random number"))
#assigning values to a
b=int(input("random number"))
#assigning values to b
print(a,b)
#printing a and b
z=a
#value of a is assigned to temporary variable z, therefore a is empty
a=b
#value of b is assigned to empty variable a, therefore b is empty 
b=z
#value of z, which initially contained value of a, is assigned to b. Therefore, the value of a and b have been shifted.
print(a,b)