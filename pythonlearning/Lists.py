dogs = ["ronny",2,True, "DAVID", "Flowey"]
print( 2 in dogs)# We can check if data is in a list using the *in* operator


print(dogs[1]) #We can get spefic values
dogs[0] = "Waty"#We can change items in the list
print(dogs)

doga =[1,"a","b",4,5,"8"]
print(doga[-4])# we can also use negative numbers to get items in a list

print(dogs[2:4]) #we can slice a list as well

print(len(dogs))#we can check the length of the list

dogs.append("marky")#We can add in a item to the list
print(dogs)

dogs.extend(["Jacob",5])# this is a way to add on another list to a current list we can also do it
#we can another list in the way dogs += ["jude", 9]
print(dogs)

dogs.remove(2)#We can remove a item to
print(dogs)

dogs.pop()#Removes the last item from the list
print(dogs)

dogs.insert( 2, "Kane")#This is a way to insert a item a spefic index
print(dogs)

dogs[2:1] = ["j", 't'] #We can also insert with slicing
print(dogs)
#Lists allow us to store multiple values of store different data types
