import banner
import math

banner.banner()

option = input("Enter ur input: ")

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
    result = math.multiplication(num1, nun2)
    print(f"ur result: ", result)
