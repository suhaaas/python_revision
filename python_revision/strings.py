str = "python"
print(str)

#   for loop
for i in str:
    print(i)

# checking if a character is in the string
if "z" in str:
    print("yes")
else:
    print("no")


print("Last character of the string is:", str[-1])

# string methods
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())

# trim and cleanup
str1  = "   python   "
print(str1.strip())
