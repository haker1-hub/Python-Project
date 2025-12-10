#================Log in==========================

print("="*80)
print("LOG IN".center(80))
print("="*80)

#===================Informatoin==================

fname = input("Enter your frist name : ").capitalize().strip()
sname = input("Enter your second name : ").capitalize().strip()
age = int(input("Enter your real age :").strip())
gmail = input("Enter your gmail :").strip()
st = input("Are you a student ?").strip().capitalize()
country = input("Enter your country :").strip().upper()
course = input("Enter course name :\n1.Python\n2.English\n3.Arabic\nHere:").capitalize()
username = gmail[:gmail.index("@")]
password = input("Write your pass word:").strip()

pw ="B1b2b3b4b5"
tries = 5
#=================frist print===================

print(f"Hello {fname} {sname}".title().center(40))

#====================While======================

while password != pw:

    tries -= 1
    print(f"Uncorrect password :-) , you have onther {'last' if tries == 0 else tries}tries.")
    password = input("Write your pass word:").strip()
 
    if tries == 0:

        break
 
    if password == pw:

        print("correct password")

#=====================if-student================

        if course in ["1","2","Python","English"] :
            
            if country == "EGYPT" :

                if st == "Yes":

                    print(f"Because you from {country} and a student \n you have discount = 50$")

                else:

                    print(f"Because you from {country} you have discount = 25$")
            elif country == "KUWAIT" :

                if st == "Yes":

                    print(f"Because you from {country}  and a student \n you have discount = 20$")

                else:

                    print(f"Because you from {country} you have discount = 5$")
            
            elif country == "KSA" :

                if st == "Yes":

                    print(f"Because you from {country}  and a student \n you have discount = 25$")

                else:

                    print(f"Because you from {country} you have discount = 10$")

            else:

                print("Sorry we don't sell course your country")

        elif course in ["Arabic","3"]:
                
            if country == "EGYPT" :

                if st == "Yes":

                    print(f"Because you from {country} and a student \n you have discount = 70$")

                else:

                    print(f"Because you from {country} you have discount = 50$")
            
            elif country == "KUWAIT" :

                if st == "Yes":

                    print(f"Because you from {country} and a student \n you have discount = 50$")

                else:

                    print(f"Because you from {country} you have discount = 25$")
            
            elif country == "KSA" :

                if st == "Yes":

                    print(f"Because you from {country} and a student \n you have discount = 55$")

                else:

                    print(f"Because you from {country} you have discount = 30$")

            else:
                

                print("Sorry we don't sell course your country")

#=====================if-age====================

        if age >= 18 :
            
            print(f"Log in successful  {username} with your gmail {gmail}")

        else:

            print(f"Don't allow to log in under limited age \n You can login after {18-age} years .")
            
#=======================final===================

        print(f"Thank you for your time {fname}")

