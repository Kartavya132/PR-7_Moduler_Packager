import math
import datetime
import random
import uuid
from sys import exit


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
                date = datetime.datetime.strptime(
                    input("Enter the date (YYYY-MM-DD): "), "%Y-%m-%d"
                )
                formats = input(f"Enter the format of date(EX: %d-%m-%Y): ")
                try:
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
                    f_curr = datetime.datetime.now()
                    while True:
                        if f_curr.minute + time_dura == datetime.datetime.now().minute:
                            break
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
                    years = float("Enter the duration in years : ")
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
                choi = input(
                    "Enter c:- circle, t:- triangle, r:- rectangle, s:- square :: "
                )
                if choi == "c":
                    rad = float(input("Enter the radius (cm): "))
                    print(f"The area is {math.pi() * rad * rad}")
                elif choi == "t":
                    side_1 = int(input("Enter the first side (cm): "))
                    side_2 = int(input("Enter the second side (cm): "))
                    side_3 = int(input("Enter the third side (cm): "))
                    s = (side_1 + side_2 + side_3) / 2
                    print(
                        f"The area is {math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))}cm"
                    )
            case "5":
                print("Thank you")
                break
            case _:
                print("Invalid Input!!")
        print("---------------------------")
    print("---------------------------")


def random_data():
    pass


def unique_id():
    pass


def files():
    pass


def attributes():
    pass


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
                exit()
            case _:
                print("Invalid choice")
                print("enter the choice as per instruction only")


def main():
    show_menu()


if __name__ == "__main__":
    main()
