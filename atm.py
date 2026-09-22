amount = 1000

user_choice = input("do you want to withdraw?, check or deposit money?: ")

if user_choice == "check balance":
    print(f"your balance is: {amount}")
elif user_choice == "deposit":
     user = int(input("input the amount to be deposited: "))
     total = amount + user
     print(f"you have successfully deposited {user}, your balance is {total} ")
elif user_choice == "withdraw":
     user = int(input("input amount to be withdraw: "))
     total = amount - user
     print(f"you just withdrawed {user}, your balance is {total}")
     if user <= 0:
        print(f"can't withdraw, please check your input")
     elif user > amount:
         print("insufficent funds man")
else:
    print("please input the write words")
    
    
        
    
    