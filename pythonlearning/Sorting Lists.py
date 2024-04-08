items=['2','5',"DAVE",'True','6','hj','bob']
items.sort() #This will sort a list of string values
print(items)

items.sort(key=str.lower)#This allows for strings with lowercases to be sorted as well properly
print(items)

print(sorted(items, key=str.lower))# This creates a new sorted list that won't affect the old list

print(items)