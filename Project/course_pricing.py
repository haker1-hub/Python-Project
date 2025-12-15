#================Log in==========================

print("="*80)
print("LOG IN".center(80))
print("="*80)

#===================Informatoin==================
age=int(input("Enter your real age \n -->"))

if age >= 18 :

    def details(first_name,second_name,gmail):

            print(f"Hello {first_name} {second_name}")
            print(f"You log in with your gmail  : {gmail}")

    first_name = input("Enter your frist name :").capitalize().strip()
    second_name = input("Enter your second name :").capitalize().strip()
    gmail = input("Enter your  gmail :")

    details(first_name,second_name,gmail)
    #password verfiy
    def verfiy(password):

          tries = 5 
          pw = input ("Enter your password to continue login \n-->")

          while pw != password: 

              tries -= 1
              print(f"Wrong pass word :-( , You have {"last"if tries == 0 else tries} tries left")
              pw = input ("Enter your password\n->")

              if tries == 0:

                  return False

          if pw == password:

              print("login in succeed :-) \n    WELCOME  ")

              return True

    verfiy("B1b2b3b4b5#")
    #price 
    pricing ={
        "Python":{
            "EGYPT":{"Yes": 70 ,
                    "No": 50
            },
            "KSA" :{"Yes": 50 ,
                    "No": 25
            },
            "KUWAIT":{"Yes": 25 ,
                    "No": 10
            }    
        },
        "English":{
            "EGYPT":{"Yes": 50 ,
                    "No": 25
            },
            "KSA" :{"Yes": 25 ,
                    "No": 15
            },
            "KUWAIT":{"Yes": 15 ,
                    "No": 5
            }    
        }
    }
    def discounts(course , country , student ):

        price = pricing[course][country][student]

        if student == "Yes":

            print(f"Because you are from {country} and a student \nYour {course} course is --> {price}$ ")

        if student == "No":

            print(f"Because you are from {country}  \nYour {course} course is --> {price}$ ")

        return price

    course = input("Enter Your course \n -->").capitalize().strip()
    country = input("Enter Your country \n -->").upper().strip()
    student = input("Are you a student ? \n -->").capitalize().strip()

    discounts(course , country , student )

    print("Thank you for your time ")

else:

    print(f"Sorry you can't login if you <18 \n You can login after { 18-age } years")
