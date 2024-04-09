#A class lets us instatisle objects

#Inhertiance
#Inhertiance is when we pass over methods from one class to another class so it can inherits those methods and properties
class Animal:
        def walk(self):
            print("Walking..")



class Dog(Animal):
    def __init__(self,name,age):#This is the constructor
        self.name = name
        self.age = age
        #The constructor all us to create multiple properties of the class


    def bark(self):
        print("Woof")
    #This is  a method of a class

roger =Dog("Gol D", 9 ) #This is how we instantise a class

print(roger.name + " " + str(roger.age))

roger.bark()
