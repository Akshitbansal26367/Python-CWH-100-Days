a = int(input("Enter a : "))
b = int(input("Enter b : "))

print("Before Swapping a = ", a, "b = ", b)
a = a + b
b = a - b
a = a - b

print("After Swapping  a = ", a, "b = ", b)
