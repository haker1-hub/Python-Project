# ===================== Calculator =====================
print("="*80)
print("Calculator".center(80))
print("="*80)

num1 = float(input("Enter number 1: "))
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

if operation == "1":
    print(num1 + num2)
elif operation == "2":
    print(num1 - num2)
elif operation == "3":
    print(num1 * num2)
elif operation == "4":
    print("Error" if num2 == 0 else num1 / num2)
elif operation == "5":
    print(num1 ** num2)
elif operation == "6":
    print("Error" if num2 == 0 else num1 // num2)
elif operation == "7":
    print("Error" if num2 == 0 else num1 % num2)
else:
    print("Error: No Operation")