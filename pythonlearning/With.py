#We use with to help with opening files as it will automaticallly close a file for us
filename = '/Users/Flavio/test.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content)