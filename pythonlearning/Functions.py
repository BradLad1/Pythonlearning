#Functions allows to create blocks of code we can call when needed

def Hello(name):  #We can add parameters
    print("Hello " + name)


Hello("Mark")  #This is an arugment that will be the value that will fill the parameter
Hello("Derek")


def defualt(name=" my Friendo"):  #We can add a default to the parameter in case we don't get a arugment to use
    print("Hello" + name)


defualt()


def Multi(name, age):  #We can add multiple parameters
    print("Hello " + name + " You are " + str(age) + " years old")


Multi("mark", 45)


#return

def returnhello(name):

    return "hi" + name


a = returnhello("jerry")
print(a)
