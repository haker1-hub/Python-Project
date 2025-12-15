#                Defind
def calculator(num1 , num2 , operation):

#                Loop

    while True:

            num1 = float(input('Enter number 1 \n -->'))
            num2 = float(input('Enter number 2  \n -->'))
            operation = input('Enter operation\n1.+\n2.-\n3.*\n4.**\n5./\n6.//\n7.%\n8.exit-->').strip().title()

#                verfity
            if type(num1)  in [float , int] and type(num2) in [float , int] :

#                System
                if operation in ["1" ,"+"]:

                      print(num1+num2)

                if operation in ["2","-"]:

                  print(num1-num2)

                if operation in ["3" ,"*"]:

                    print(num1*num2)

                if operation in ["4" ,"**"]:

                    print(num1**num2)

                if operation in ["5","/"]:

                    if num2 == 0 :

                        print("Erorr")

                    else:

                        print(num1/num2)

                if operation in ["6","//"]:

                    if num2 == 0 :

                        print("Erorr")

                    else:   

                        print(num1//num2)

                if operation in ["7","%"]:

                    if num2 == 0 :

                        print( "Erorr")

                    else:

                        print(num1%num2)

                if operation in ["Exit","8"]:

                    print("Good bye")
                    break

            if type(num1) in  [ str,bool,list,dict,set] or type(num2)  in [str,bool,list,dict,set] : 

                print("You can use float and integer number only try again.")

#            variable
num1 = float(input('Enter number 1  \n -->'))
num2 = float(input('Enter number 2  \n -->'))
operation = input('Enter operation\n1.+\n2.-\n3.*\n4.**\n5./\n6.//\n7.%\n8.exit-->').strip().title()

calculator(num1 , num2 , operation)

