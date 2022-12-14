#calculator
import math
x = int(input("please insert an integer: "))
op = input("please select the operation(radical, sin, cos, tan, cot, factorial): ")
radical = math.sqrt(x)
sin = math.sin(x)
cos = math.cos(x)
tan = math.tan(x)
cot = (math.cos(x) * math.sin(x))
factorial = math.factorial(x)

if op == "radical":
    result = radical
if op == "sin":
    result = sin
if op == "cos":
    result = cos
if op == "tan":
    result = tan
if op == "cot":
    result = cot
if op == "factorial":
    result = factorial


print(result)