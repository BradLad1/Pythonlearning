 #recursion
 #Recursion is when a function calls itself
#To not get a recursion we need a base case to stop the recursion from constantly going on
def factorial(n):
    if n==1: return 1#base case
    return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6 ))
