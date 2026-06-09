import banner
import math

banner.banner()

option = input("Enter ur option: ")

num1 = input("Enter ur first num: ")
num2 = input("Enter ur second num: ")
num1 = int(num1)
num2 = int(num2)

if option == "1":
    result = math.plus(num1, num2)
    print(f"ur result: ", result)
elif option == "2":
    result = math.minus(num1, num2)
    print(f"ur result: ", result)
elif option == "3":
    result = math.multiplication(num1, num2)
    print(f"ur result: ", result)
elif option == "4":
    if num2 == 0:
        print("sorry cannot divide by zero :)")
    else:
        result = math.division(num1, num2)
        print(f"ur result: ", result)
elif option == "5":
    print("Square root only support one number")
    num1 = input("Enter a num: ")
    num1 = int(num1)
    result = math.square(num1)

    print(f"ur result: ", result)
else:
    print("What you enterd pls enter 1-5. 😜")