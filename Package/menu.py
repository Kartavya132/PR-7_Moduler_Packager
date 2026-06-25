def menu_build(*arg):
    menu = arg
    print(f"\n\n------{menu[0]}------")
    try:
        for i in range(1, len(menu)):
            print(f"{i}. {menu[i]}")
        print("-" * (12 + len(menu[0])))
        return input("Enter your choice : ")
    except Exception:
        print("Enter the choice properly")
