 #Loops will reapeat code

 #There are two types of loops while loops and for loops

 #while loops
#While loops will loop untill the condition is false
conditon = True

while conditon:
     print("conditon is true")
     break
#This is an exmaple of a while loop and an infinte loop

count =0
while count <10:
    print("counting to " + str(count))
    count +=1 # We usually use a counter to stop a while loop from running infintely
 #while loops

#For Loops
#A for loops are count controlled and loops for a set amount of times
items = [1,2,3,4,5]
for item in items:#will loop through the whole list then will stop
    print(item)

for item in range(15):#This will loop in range of 15
    print(item)

items2 =[2,4,6,8,10]
for item2 in enumerate(items2): #using enumerate will return the index and the item
    print(item2)
#For Loops



