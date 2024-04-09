#Sets are like tuple but they ordered and can be changed at runtime

names1={"Roger", "Syd", "ape"}
names2={"Roger"}

modific = names1 | names2 # | is used how we put two sets together
instercet = names1 & names2 # & Is used to get the intersect of two sets
dif = names1 - names2 # - is used to find the difference between two sets
lower = names1 < names2
higher = names1 > names2
# < and >  used to see if one set has more items than the other
print(instercet)
print(modific)
print(dif)
print(lower)
print(higher)
print(list(names2))#turns a set into a list

#A set can't have two of the same item