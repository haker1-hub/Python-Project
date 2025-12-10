# ===================== Calculator =====================

print("="*80)
print("Calculator".center(80))
print("="*80)

#====================In put============================
num1 = input("Enter number 1: ").strip().capitalize()
#========================If=============================
while num1 != "Exit":

    num1 = input("Enter number 1: ").strip().capitalize()
    num2 = float(input("Enter number 2: "))
    operation = input("""Choose operation:
    1. +
    2. -
    3. *
    4. /
    5. **
    6. //
    7. %
    = """)
    if num1 == "Exit":

        print("Thank you for your time")

        break

    if operation in ["1","+"]:

        print(float(num1) + num2)

    elif operation in ["2","-"]:

        print(float(num1) - num2)

    elif operation in ["3","*"]:

        print(float(num1) * num2)

    elif operation in ["4","/"]:

        print("Error" if num2 == 0 else float(num1) / num2)

    elif operation in ["5","**"]:

        print(float(num1) ** num2)

    elif operation in ["6","//"]:

        print("Error" if num2 == 0 else float(num1) // num2)

    elif operation in ["7","%"]:

        print("Error" if num2 == 0 else float(num1) % num2)

    else:

        print("Error:) Try again")


