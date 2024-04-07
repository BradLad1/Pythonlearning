 #Booleans have two values of True and False

done =True
undone =False

#All numbers are true expect 0
#Strings are true but empty strings are false
if done:
    print("yes")
else:
    print('no')


is_it_finshed =any([done, undone]) #the any() function checks if any of the values are True
print(is_it_finshed)

aretheydone = all([done,undone])
print(aretheydone)
#SLICING