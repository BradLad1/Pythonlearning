items = [1,2,3,4,5]
for item in items:#will loop through the whole list then will stop
    if item==2:
        continue
    print(item)
    #continue will stop the current iteration and tell python execute the next one
    #break stops the loop and tells the program to move onto the next line