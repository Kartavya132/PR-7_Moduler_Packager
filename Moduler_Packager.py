import math
import datetime
import random
import uuid
import sys


def menu_build(*arg):
    menu = arg
    print(f"\n\n------{menu[0]}------")
    try:
        for i in range(1, len(menu)):
            print(f"{i}. {menu[i]}")
        print("-" * (12 + len(menu[0])))
        return input("Enter your choice : ")
    except:
        print("Enter the choice proper")


def date_time():
    while True:
        choi = menu_build(
            "Date-Time Menu",
            "Display current date and time",
            "Calculate difference between two date",
            "Format date into custom format",
            "Stopwatch",
            "Countdown timer",
            "Back to Main Menu",
        )
        match choi:
            case "1":
                print(f"Current Date and time is {datetime.datetime.now()}")
            case "2":
                first = input("Enter the first date (YYYY-MM-DD): ")
                second = input("Enter the second date (YYYY-MM-DD): ")
                try:
                    diff_date = datetime.datetime.strptime(
                        second, "%Y-%m-%d"
                    ) - datetime.datetime.strptime(first, "%Y-%m-%d")
                    print(f"The difference :: {diff_date.days} day/s")
                except:
                    print("Invalid Date")
            case "3":
                try:
                    date = datetime.datetime.strptime(
                        input("Enter the date (YYYY-MM-DD): "), "%Y-%m-%d"
                    )
                    formats = input("Enter the format of date(EX: %d-%m-%Y): ")
                    print(f"Formatted date :: {date.strftime(formats)}")
                except ValueError:
                    print("You Enter invalid format!!")
            case "4":
                print("To start stopwatch, Press : Enter", end="")
                input()
                current = datetime.datetime.now()
                print("Press : Enter, to stop", end="")
                input()
                end = datetime.datetime.now()
                print(f"The stopped: {end-current}")
            case "5":
                try:
                    time_dura = int(input("Enter the duration(minutes) : "))
                except ValueError:
                    print("Invalid Input")
                else:
                    end_time = datetime.datetime.now() + datetime.timedelta(
                        minutes=time_dura
                    )
                    while datetime.datetime.now() < end_time:
                        pass
                    print(f"{time_dura} min is passed")
            case "6":
                print("Thank you")
                break
            case _:
                print("Invalid choice")
        print("---------------------------")
    print("---------------------------")


def mathematic():
    while True:
        choi = menu_build(
            "Maths Operations",
            "Calculate Factorial",
            "Solve Compound Interest",
            "Trigonometric Operations",
            "Area of geometric Shapes",
            "Back to Main Menu",
        )
        match choi:
            case "1":
                try:
                    num = int(input("Enter the number : "))
                    fact = math.factorial(num)
                    print(f"The factorial of {num} is {fact}")
                except:
                    print("Invalid Input")
            case "2":
                try:
                    principal = int(input("Enter the pricipal amm. : "))
                    rate = float(input("Enter the rate of interest : "))
                    years = float(input("Enter the duration in years : "))
                    total_ammount = principal * (1 + rate / 100) ** years
                    print(f"The Total Ammount is ${total_ammount}")
                except ValueError:
                    print("Invalid Input!!")
            case "3":
                tri = input("Enter s:- sin, c:- cos, t:- tan :: ")
                try:
                    angle = float(input("Enter the angle : "))
                except ValueError:
                    print("Invalid Input!!")
                else:
                    angle = math.radians(angle)
                    if tri == "s":
                        print(f"Sin {angle}` is {math.sin(angle)}")
                    elif tri == "c":
                        print(f"Cos {angle}` is {math.cos(angle)}")
                    elif tri == "t":
                        print(f"Tan {angle}` is {math.tan(angle)}")
            case "4":
                fig = input(
                    "Enter c:- circle, t:- triangle, r:- rectangle, s:- square :: "
                )
                if fig == "c":
                    try:
                        rad = float(input("Enter the radius (cm): "))
                        print(f"The area is {math.pi * rad * rad}")
                    except ValueError:
                        print("Invalid Input!!")
                elif fig == "t":
                    try:
                        side_1 = int(input("Enter the first side (cm): "))
                        side_2 = int(input("Enter the second side (cm): "))
                        side_3 = int(input("Enter the third side (cm): "))
                        s = (side_1 + side_2 + side_3) / 2
                        print(
                            f"The area is {math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))}cm"
                        )
                    except ValueError:
                        print("Invalid Input!!")

                elif fig == "r":
                    try:
                        a = int(input("Enter the lenght : "))
                        b = int(input("Enter the breadth : "))
                    except ValueError:
                        print("Invalid Input!!")
                    else:
                        print(f"The area is {a*b}")
                elif fig == "s":
                    try:
                        side = float(input("Enter the side (cm) : "))
                        print(f"The area is {side * side}")
                    except ValueError:
                        print("Invalid Input!!")
                else:
                    print("Invalid choice!!")
            case "5":
                print("Thank you")
                break
            case _:
                print("Invalid Input!!")
        print("---------------------------")
    print("---------------------------")


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
                    dig = int(input("Enter the number of digit : "))
                except:
                    print("Invalid Input!!")
                else:
                    print(f"The random number is {random.randint(0,(10**dig))}")
            case "2":
                lists = []
                try:
                    n = int(input("Enter the length of list : "))
                except:
                    print("Invalid Input!!")
                else:
                    for _ in range(1, n + 1):
                        lists.append(random.randint(1, 10))
                    print("The random generated lists is:\n:- ", end="")
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
                except:
                    print("Invalid Input!!")
                else:
                    for _ in range(0, lent):
                        password += random.choice(char)
                    print(f"The random generated password : {password}")
            case "4":
                otp = ""
                try:
                    lent = int(input("Enter the lenght of OTP : "))
                except:
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
    print("------------------------")


def unique_id():
    print("Generate Unique ID ::-")
    my_uuid = uuid.uuid4()
    print(f"ID:- {my_uuid}")
    print("Thank you!, Press Enter to continue")
    input()


def files():
    while True:
        choi = menu_build(
            "File Operation",
            "Create a new file",
            "Write to a file",
            "Read from a file",
            "Append to a file",
            "back to Main Menu",
        )

        match choi:
            case "1":
                file_name = input("Enter the name of the file : ")
                try:
                    with open(file_name, "x"):
                        pass
                    print("The file is created!!")
                except ValueError:
                    print("Invalid Input!!")
                except FileExistsError:
                    print("file already exists make new file")
            case "2":
                file_name = input("Enter the file name to write : ")
                print("Enter what to write, below ( '.' is used for seperation) : ")
                work = input(":-").split(".")
                write = ""
                for item in work:
                    write += item + ".\n"
                try:
                    with open(file_name, "w") as f:
                        f.write(write)
                    print("The lines are written")
                except:
                    print("Invalid Input, try again")
            case "3":
                file_name = input("Enter the file name to read : ")
                try:
                    with open(file_name, "r") as f:
                        reads = [lines for lines in f.readlines()]
                except ValueError:
                    print("Invalid Input!!")
                except FileNotFoundError:
                    print("There si no such file!")
                else:
                    if reads:
                        print("The lines in file is ::-")
                        for line in reads:
                            print(line, end="")
                        print("\nAll lines is readed")
                    else:
                        print("There is no data")
            case "4":
                file_name = input("Enter the file name to append : ")
                print("Enter what to append, below ( '.' is used for seperation) : ")
                work = input(":-").split(".")
                write = ""
                for item in work:
                    write += item + ".\n"
                try:
                    with open(file_name, "a") as f:
                        f.write(write)
                    print("The lines added")
                except:
                    print("Invalid Input, try again")
            case "5":
                print("Thank you")
                break
            case _:
                print("Invalid Input!!")
        print("------------------------")
    print("------------------------")


def attributes():
    module = input("Enter the module you want to enter : ")
    if module in "math":
        attribute = dir(math)
    elif module in "random":
        attribute = dir(random)
    elif module in "datetime":
        attribute = dir(datetime)
    elif module in "uuid":
        attribute = dir(uuid)
    elif module in "sys":
        attribute = dir(sys)
    else:
        print("Invalid module")
        print("---------------------")
        return
    print("The Attributes are :-\n[", end="")
    for i in range(0, 20):
        print(f"{attribute[i]}, ", end="")
    print("...}")

    print("------------------------")


def show_menu():
    while True:
        print("------------------------------")
        print("| Welcome to omni-media tool |")
        print("------------------------------\n")

        print("------Main Menu------")
        print("1. Datetime and Time Operations")
        print("2. Mathematical  Operations")
        print("3. Random Data Generator")
        print("4. Generate Unique id(UUID)")
        print("5. File Operations")
        print("6. Attributes explore")
        print("7. Exit")
        print("---------------------")
        choice = input("Enter your choice : ")

        match choice:
            case "1":
                date_time()
            case "2":
                mathematic()
            case "3":
                random_data()
            case "4":
                unique_id()
            case "5":
                files()
            case "6":
                attributes()
            case "7":
                print("Thank for using me!!")
                print("Good Bye")
                sys.exit()
            case _:
                print("Invalid choice")
                print("Enter the choice as per instruction only")
        print("====================")


def main():
    show_menu()


if __name__ == "__main__":
    main()
