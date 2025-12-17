#        Defind
def age_converter(age):    
#        Varible
    month = age * 12
    week = age * 52
    day = week * 7
    hour = day * 24
    minute = hour * 60
    future= 80 + age
#        Loop
    while True:

        op=input("Enter the time operation\n1.Months  2.Weeks  3.Days\n4.Hours  5.minutes  6.After 80\n7.Exit\n-->").capitalize().strip() 

        if op in ["1","Months","Month"] :

            print(f"You lived {month:,} months.")

        elif op in ["2","Weeks","Week"]:

            print(f"You lived {week:,} weeks.")

        elif op in ["3","Days","Day"]:

            print(f"You lived {day:,} days.")

        elif op in ["4","Hours","Hour"]:

            print(f"You lived {hour:,} hours.")

        elif op in ["5","minutes","minutes"]:

            print(f"You lived {minute:,} minutes.")

        elif op in ["6","future"]:

            print(f"You will be {future:,} years old after 80 year.")

        elif op in  ["7","Exit"]:

            print("Good bye I wish a good life to you :-)")

            break

        else:

            print("Sorry try again ")
#        In Put
age = int(input("Enter your age -->"))
#        Defind End
age_converter(age)
