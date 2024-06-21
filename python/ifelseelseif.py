# mark=int(input("enter marks"))
# if mark >= 80 and mark <= 100:
#  print("you have an A")  
# elif mark >=60 and mark <80:
#  print("you have a B")
# elif mark >=40 and mark <60:
#  print("you have a c")
# elif mark >=0 and mark <40:
#  print("you have failed terribly")
# else:
#     print("wrong inputs check marks")

num1=int(input("enter number"))
num2=int(input("enter number"))
num3=int(input("enter number"))
num4=int(input("enter number"))
if num1>num2 and num1>num3 and num1>num4:
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3 and num2>num4:
    print(f"{num2} is the largest number")
elif num3>num1 and num3>num2 and num3>num4:
    print(f"{num3} is the largest number")
elif num4>num1 and num4>num2 and num4>num3:
    print(f"{num4} is the largest number")
else:
    print("all numbers are the same")
  