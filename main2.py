string, dict = str(input("Input a string:")), {}
for char in set(string):
    dict[char] = string.count(char)
print(dict)
