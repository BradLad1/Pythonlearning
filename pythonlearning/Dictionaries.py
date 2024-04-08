dog={"name":"jEFF" ,"Owner":"Sally", "age":8, "colour":"green"}
print(dog)

dog["name"] ="Kane"#This is how we change the value in dictionary
print(dog)

print(dog.get("name"))#This will get spefic values and we can check if value are in there

print(dog.get("colur", "red")) #If we don#t find a value in get we can set a default value in this cause red since we don't have the colour key

print(dog.pop("name"))#We can remove a key value pair with key:value .pop()
print(dog)
print(dog.popitem())#This will remove the last key:value pair
print(dog)

print("colour" in dog) #We can use the in stament on a dictionary


print(dog.keys())#This can show us all the keys in a dictionary
print(list(dog.keys()))#We can use the list() function to return just the list

print(dog.values())#This will return out all the values
print(list(dog.values()))#This return a the values as a list

dog["Favourite food"]="Meat" #This is how we add a key:value pair the dictionary
print(dog)

del dog["Owner"]#This is how we delete a key;value pair
print(dog)

dogCopy =dog.copy()#This is how we copy a dictionary
print(dogCopy)
#A dictionary is key:value pairs