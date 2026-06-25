import random
from .menu import menu_build

def random_data():
    while True:
        choi = menu_build(
            "Random data Generator",
            "Generate random number",
            "Generate random list",
            "Create random password",
            "Generate Random OTP",
            "Back to Main Menu",
        )
        match choi:
            case "1":
                try:
                    dig = int(input("Enter the number of digits : "))
                except Exception:
                    print("Invalid Input!!")
                else:
                    print(f"The random number is {random.randint(0, (10**dig))}")
            case "2":
                lists = []
                try:
                    n = int(input("Enter the length of list : "))
                except Exception:
                    print("Invalid Input!!")
                else:
                    for _ in range(1, n + 1):
                        lists.append(random.randint(1, 10))
                    print("The random generated list is:\n:- ", end="")
                    for i in lists:
                        print(f"{i}", end=" ")
                    print()
            case "3":
                char = "abcdefghijklmnopqrstuvwxyz"
                char += char.upper()
                char += "1234567890!@#$%+-_=&*"
                password = ""
                try:
                    lent = int(input("Enter the length of password : "))
                except Exception:
                    print("Invalid Input!!")
                else:
                    for _ in range(0, lent):
                        password += random.choice(char)
                    print(f"The random generated password : {password}")
            case "4":
                otp = ""
                try:
                    lent = int(input("Enter the length of OTP : "))
                except Exception:
                    print("Invalid Input!!")
                else:
                    for _ in range(0, lent):
                        otp += str(random.randint(0, 9))
                    print(f"The random generated otp : {otp}")
            case "5":
                print("Thank you")
                break
            case _:
                print("Invalid Input!!")
        print("------------------------")
