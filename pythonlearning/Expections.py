#Expections are used to handle errors


try:#this is where we put the code:
    result = 2 / 0
    print(result)
except ZeroDivisionError:#this is where put the error handler
    print("can't divide by zero")

finally:#The code in the finally block always run
    result=1
    print(result)

raise Exception('An error nigga')#This will raise expection and show us an error message