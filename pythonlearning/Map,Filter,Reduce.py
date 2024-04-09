#map()
#map() is used to apply a specifed function to iterable
#iterable e.g lists, tuples, dictionaries and sets

nums =[1,2,3]

def double(a):
    return a*2

result = map(double,nums) #Here the double function is applied on all the nums

result_list =list(result)#we turn the map object back into a list so we can print it
print(result_list)

#done with lamba
nums2 =[9,5,3]
result = map(lambda b: b*2,nums2) #Here the double function is applied on all the nums

result_list2 =list(result)#we turn the map object back into a list so we can print it
print(result_list2)

#Filter()
#The filter function will take iterable and return the filter object which is another iterable without some of the items
testnum = [1, 8,2, 3]
def isEven(a):
    return a%2==0

result = filter(isEven,testnum) #Here we return the iterable but now some items will be taken out
print(list(result))


#With Lamba
testnum = [1, 8,2, 3]

result = filter(lambda b: b%2==0,testnum) #Here we return the iterable but now some items will be taken out
print(list(result))

#In simple terms filter we filter out some infomation


#reduce
#Reduce is used to calculate the value out of a sequence
from functools import  reduce
expenses =[
    ('Dinner',90),
    ('Car Repair', 120)
]

sum = reduce(lambda a,b: a[1]+b[1], expenses)
print(sum)