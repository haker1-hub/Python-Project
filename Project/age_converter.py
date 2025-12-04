# ===================== Age Calculator =====================

print("=" * 80)
print("You can write the number or full word".center(80))
print("=" * 80)

# =====================in put===============================

age = int(input("Enter your age: "))
op = input("Choose operation:\n1.month\n2.week\n3.day\n4.hour\n5.minute\n6.When will you be 80 years?\n= ").lower()

# ========================variable===========================

month = age * 12
week = age * 52
day = week * 7
hour = day * 24
minute = hour * 60
future= 80 - age

# =========================If==================================

if op in ["1", "month"]:

    print(f"You lived {month:,} months.")

elif op in ["2", "week"]:

    print(f"You lived {week:,} weeks.")

elif op in ["3", "day"]:

    print(f"You lived {day:,} days.")

elif op in ["4", "hour"]:

    print(f"You lived {hour:,} hours.")

elif op in ["5", "minute"]:

    print(f"You lived {minute:,} minutes.")

elif op in ["6","When you will be 80 years?"]:

    print(f"You will be 80 years after {future:,} years.")
    
else:

    print("Use valid operation only.")
