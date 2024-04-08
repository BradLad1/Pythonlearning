#Nested functions are functions inside of functions and can only be seen by that function

def talk(pharse):
    def say(word):
        print(word)

    words = pharse.split(' ')# .split('') is used to create a list out of a string
    for word in words:
        say(word)
talk("He going to fight me")


def count():
    count =0

    def incremnt():
        nonlocal count #the nonlocal is used to
        count =count+1
        print(count)

    incremnt()
count()

#Closures
#Closures are used
