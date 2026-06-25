import math
import random
import datetime
import uuid
import sys

def attributes():
    module = input("Enter the module you want to explore (math, random, datetime, uuid, sys) : ").strip().lower()
    if module == "math":
        attribute = dir(math)
    elif module == "random":
        attribute = dir(random)
    elif module == "datetime":
        attribute = dir(datetime)
    elif module == "uuid":
        attribute = dir(uuid)
    elif module == "sys":
        attribute = dir(sys)
    else:
        print("Invalid module")
        print("---------------------")
        return

    print("The Attributes are :-")
    print("[", end="")
    # Safely print up to 20 items or the length of the list, whichever is smaller
    limit = min(20, len(attribute))
    for i in range(limit):
        print(f"{attribute[i]}, ", end="")
    print("...]")
    print("------------------------")
