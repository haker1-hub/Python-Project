# ===================== Format String =====================

name = "belal"
age = 20
level = "legendry"

print(f"""My name is : {name}
My age is : {age}
My level is : {level}""")

# ===================== Login =====================

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gmail = input("Enter your gmail: ")
password = input("Enter your password: ")

the_username = gmail[:gmail.index("@")]

print(f"Hello {name.capitalize()}")

if age >= 18:

    print(f"Login success with your gmail: {gmail}\nHave a nice day {the_username}")

else:

    print("Don't allow to login under the limited age")