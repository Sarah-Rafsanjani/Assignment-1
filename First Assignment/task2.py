a = (int(input("please enter the first side: ")))
b = (int(input("please enter the second side: ")))
c = (int(input("please enter the third side: ")))

if (a + b > c) and (b + c > a) and (a + c > b):
    result = "these numbers can be three sides of a triangle."
else:
    result = "these numbers cannot be three sides of a triangle."

print(result)