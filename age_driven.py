name = input("what is your name?: ")

user_age = int(input("how old are you?: "))

if user_age >= 18:
    print(f"{name}, you can apply for a drivers license")
elif user_age >=70:
    print(f"{name}, you may need a medical check")
else:
    print(f"{name}, you are too young to drive")