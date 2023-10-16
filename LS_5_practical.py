Enter_name = input("Enter your name ")
print("your name is ", Enter_name)
print(type(Enter_name))

Enter_number = input("Enter the number ")
print("Number is ",Enter_number)
print(type(Enter_number)) #By Default it string

Enter_no = int(input("Enter a number"))
print(type(Enter_no))

print("Operation")
a = int(input("Enter a first number "))
b = int(input("Enter a second number "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)

eno = int(input("Enter Employee No "))
enum = input("Enter Employee name ")
esal = float(input("Enter a salary "))
ecity = input("Enter Employee city ")
married = bool(input("is employee married ? "))
print("Employee number ",eno)
print("Employee name ",enum)
print("Employee salary ",esal)
print("Employee city ",ecity)
print("Employee married ", married)

print('x','y','z',sep="#")

print("xyz",end="@")
