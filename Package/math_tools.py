import math
from .menu import menu_build

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
                except Exception:
                    print("Invalid Input")
            case "2":
                try:
                    principal = int(input("Enter the principal amount : "))
                    rate = float(input("Enter the rate of interest : "))
                    years = float(input("Enter the duration in years : "))
                    total_amount = principal * (1 + rate / 100) ** years
                    print(f"The Total Amount is ${total_amount:.2f}")
                except ValueError:
                    print("Invalid Input!!")
            case "3":
                tri = input("Enter s:- sin, c:- cos, t:- tan :: ")
                try:
                    angle = float(input("Enter the angle in degrees: "))
                except ValueError:
                    print("Invalid Input!!")
                else:
                    angle_rad = math.radians(angle)
                    if tri == "s":
                        print(f"Sin {angle}° is {math.sin(angle_rad)}")
                    elif tri == "c":
                        print(f"Cos {angle}° is {math.cos(angle_rad)}")
                    elif tri == "t":
                        print(f"Tan {angle}° is {math.tan(angle_rad)}")
                    else:
                        print("Invalid trigonometric choice")
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
                        area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
                        print(f"The area is {area} cm²")
                    except ValueError:
                        print("Invalid Input!!")
                elif fig == "r":
                    try:
                        a = int(input("Enter the length : "))
                        b = int(input("Enter the breadth : "))
                    except ValueError:
                        print("Invalid Input!!")
                    else:
                        print(f"The area is {a * b}")
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
