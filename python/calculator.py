# 1.add
# 2. subtract
# 3.multiplication
# 4. division
print("select an operation to perform:")
print("1.add")
print("2.subtract")
print("3.multiplication")
print("4.division")

operation=input()
if operation=="1":
    num1=input("enter first number")
    num2=input("enter second number")
    print("the sun is" +str(int(num1)+int(num2)))
    # code for add

elif operation=="2":
    num1=input("enter first number")
    num2=input("enter second number")
    print("the sun is" +str(int(num1)-int(num2)))
    # code for subtract

elif operation=="3":
    num1=input("enter first number")
    num2=input("enter second number")
    print("the sun is" +str(int(num1)*int(num2)))
    # code for multiplication

elif operation=="4":
    num1=input("enter first number")
    num2=input("enter second number")
    print("the sun is" +str(int(num1)/int(num2)))
    # code for division

else:
    print("invalid entry")
