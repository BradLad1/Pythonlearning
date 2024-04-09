#A Decorator is a way to a way to change,enhance or alter how a function works

#A decorator will wrap up a function
#we use decrators to change the behaviour of a function without modifying it

def longtime(func):
    def wrapper():
        print("before")
        val=func()
        print("after")
        return val
    return wrapper



@longtime
def hello():
    print("hello")

hello()