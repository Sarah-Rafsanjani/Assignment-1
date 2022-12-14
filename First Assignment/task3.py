name = input("please enter your name: ")
lastname = input("please enter your last name: ")
x = float(input("please enter your math score: "))
y = float(input("please enter your science score: "))
z = float(input("please enter your literature score: "))

average = float((x + y + z) / 3)
print ("dear", name, lastname, "your average is:", average)

if average >= 17:
    print("your status is great.")
if 12 <= average < 17:
   print("your status is normal.")
if average < 12:
    print("your status is failed.")