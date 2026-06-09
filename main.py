import banner
import math

banner.banner()

while True:
    option = input("\nEnter ur option (1-6): ").strip().lower()

    if option in ("6", "exit", "q", "quit"):
        print("Goodbye! Thank you for using Beautiful Calc :)")
        break

    if option in ("1", "2", "3", "4"):
        num1 = input("Enter ur first num: ")
        num2 = input("Enter ur second num: ")
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("Invalid input! Please enter integers.")
            continue

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
        num1 = input("Enter a num: ")
        try:
            num1 = int(num1)
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue
        result = math.square(num1)
        print(f"ur result: ", result)

    else:
        print("What you enterd pls enter 1-6. 😜")