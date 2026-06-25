import datetime
from .menu import menu_build

def date_time():
    while True:
        choi = menu_build(
            "Date-Time Menu",
            "Display current date and time",
            "Calculate difference between two dates",
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
                except ValueError:
                    print("Invalid Date")
            case "3":
                try:
                    date = datetime.datetime.strptime(
                        input("Enter the date (YYYY-MM-DD): "), "%Y-%m-%d"
                    )
                    formats = input("Enter the format of date (EX: %d-%m-%Y): ")
                    print(f"Formatted date :: {date.strftime(formats)}")
                except ValueError:
                    print("You entered an invalid format!!")
            case "4":
                print("To start stopwatch, Press : Enter", end="")
                input()
                current = datetime.datetime.now()
                print("Press : Enter, to stop", end="")
                input()
                end = datetime.datetime.now()
                print(f"The stopped time: {end - current}")
            case "5":
                try:
                    time_dura = int(input("Enter the duration (minutes) : "))
                except ValueError:
                    print("Invalid Input")
                else:
                    end_time = datetime.datetime.now() + datetime.timedelta(
                        minutes=time_dura
                    )
                    while datetime.datetime.now() < end_time:
                        pass
                    print(f"{time_dura} min has passed")
            case "6":
                print("Thank you")
                break
            case _:
                print("Invalid choice")
        print("---------------------------")
