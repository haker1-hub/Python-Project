# ===================== Course System =====================
Name = input("Enter your name: ")
country = input("Enter your country: ").capitalize().strip()
Isstudent = input("Are you a student? ").capitalize().strip()

Course = "Python Course"
price = 1000

print("=" * 80)

if country == "Egypt":
    print(f"Hello {Name}")
    if Isstudent == "Yes":
        print(f"You are student. Price: {(price*0.75)*47:,} جنيه")
    else:
        print(f"Price: {(price*0.5)*47:,} جنيه")

elif country == "KSA":
    print(f"Hello {Name}")
    if Isstudent == "Yes":
        print(f"Price: {(price * 0.25) / 0.27:,} ريال")
    else:
        print(f"Price: {price / 0.27:,} ريال")

elif country == "Kuwait":
    print(f"Hello {Name}")
    print(f"Price: {price/3.26:,} دينار كويتي")

elif country == "Qatar":
    print(f"Hello {Name}")
    print(f"Price: {price/0.27:,} ريال قطري")

elif country == "Algerian":
    print(f"Hello {Name}")
    if Isstudent == "Yes":
        print(f"Price: {price*0.65*130.21:,} دينار جزائري")
    else:
        print(f"Price: {price*0.5*130.21:,} دينار جزائري")

else:
    print("Sorry, we don't sell in your country.")
