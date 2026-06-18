import math
import datetime
import random
import uuid
from sys import exit


def menu_build(*arg):
    menu = arg
    print(f"-----{menu[0]}-----")
    try:
        for i in range(1, len(menu)):
            print(f"{i}. {menu[i]}")
        print("-" * (10 + len(menu[0])))
        return input("Enter your choice : ")
    except:
        print("Enter the choice proper")


def date_time():
    choi = menu_build("Date-Time Menu")


def mathematic():
    pass


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
