import sys
from omni_utils import (
    date_time,
    mathematic,
    random_data,
    unique_id,
    files,
    attributes
)

def show_menu():
    while True:
        print("------------------------------")
        print("| Welcome to omni-media tool |")
        print("------------------------------\n")

        print("------Main Menu------")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
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
                print("Thanks for using me!!")
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
