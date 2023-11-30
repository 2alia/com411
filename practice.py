try:
    age = int (input("please enter age:"))
    print(f" the age is {age}")
except ValueError:

    print("please enter a number")
except:

    print("Huh")