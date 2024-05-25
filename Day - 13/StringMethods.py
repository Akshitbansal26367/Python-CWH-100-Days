# Strings are immutable i.e. they cannot be changed (inplace)
a = "!!!Harry!!!! Harry Harry"
print("Original String is", a)
print("Upper Case String is", a.upper())
print("Lower Case String is", a.lower())
# Removes trailing spaces
print("Trailed end string is", a.rstrip("!!!!!"))
# replace all occurrences of Harry
print("Removed Harry with John", a.replace("Harry", "John"))
# this method splits the given string at the specified instance and returns the separated string as list items
print("List is", a.split(" "))
# this method turns only the first character of the string to uppercase and the rest other characters of the string
# are turned to lowercase. The string has no effect if the first character is already uppercase.
blogHeading = "introduction tO js"
print("First capital letter is", blogHeading.capitalize())
str1 = "Welcome to the Console!!!"
print("The centered string is ", str1.center(70))
