names = "HarryShubham"
print("Length is", len(names))  # prints length of string
print("Characters from 0 to 6 are ", names[0:7])  # prints characters from index 0 to n - 1 (0 to 6)
print("Characters from 1 to 4 are ", names[1:5])  # prints characters from index 1 to n - 1 (1 to 4)
print(names[0:-3])  # prints names[0:len(names)-3] i.e. names[0:9] prints from index 0 to 8
print(names[-3:-1])  # prints names[len(names)-3:len(names)-1] i.e. names[9:11] prints from index 9 to 10

# Quick Quiz :
nm = "Harry"
print(nm[-4:-2])  # prints nm[len(nm) - 4:len(nm) - 2] i.e. nm[1:3] prints from index 1 to 2
