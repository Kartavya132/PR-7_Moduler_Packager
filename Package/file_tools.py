from .menu import menu_build

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
                    print("File already exists, make a new file")
            case "2":
                file_name = input("Enter the file name to write : ")
                print("Enter what to write below ('.' is used for separation) : ")
                work = input(":-").split(".")
                write = ""
                for item in work:
                    if item.strip():
                        write += item.strip() + ".\n"
                try:
                    with open(file_name, "w") as f:
                        f.write(write)
                    print("The lines are written")
                except Exception:
                    print("Invalid Input, try again")
            case "3":
                file_name = input("Enter the file name to read : ")
                try:
                    with open(file_name, "r") as f:
                        reads = [line for line in f.readlines()]
                except ValueError:
                    print("Invalid Input!!")
                except FileNotFoundError:
                    print("There is no such file!")
                else:
                    if reads:
                        print("The lines in file are ::-")
                        for line in reads:
                            print(line, end="")
                        print("\nAll lines read successfully")
                    else:
                        print("There is no data")
            case "4":
                file_name = input("Enter the file name to append : ")
                print("Enter what to append below ('.' is used for separation) : ")
                work = input(":-").split(".")
                write = ""
                for item in work:
                    if item.strip():
                        write += item.strip() + ".\n"
                try:
                    with open(file_name, "a") as f:
                        f.write(write)
                    print("The lines added")
                except Exception:
                    print("Invalid Input, try again")
            case "5":
                print("Thank you")
                break
            case _:
                print("Invalid Input!!")
        print("------------------------")
