string = str(input("Input a string:"))
print({key: string.count(key) for key in string})
