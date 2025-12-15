#     Function

def name():

    return"hello function"

print(name())

#============================
a , b  ="belal" , "waleed"
def hello (name):

    print(f"hello {name}")

hello(a)
hello("waleed")

def num (n1 , n2):

    if type(n1) == int and type(n2) == int:

        print(n1 * n2)

    else:

        print("you can use integer only")

num(3,6)

def n(f,m,t):

    print(f"hello {f.capitalize().strip()}.{m .upper():.1s} {t.capitalize()} ")

n("belal","waleed","ahmed")
#============================
def detials(name,*skills):

    print(f"hello {name} your skill is :")

    for skill in skills :

        print("-" + skill)

detials("belal","python","css")
#=======================
def detials(name, country, age="unkown" ):

    print(f"hello {name.capitalize()}\nyour age is {age}\nand your country is {country}")

detials("belal","egypt",39)
detials("belal","ksa")
#============================
def show_skill(**skills):

    for skill , value  in skills.items():

        print(f'Your skill is :')
        print(f'-{skill} => {value}%')

show_skill(python =50,css=89,html=14)

#another code dict
myskill={"python" :50,
        "css":89,
        "html":14
}
def show_skill(**skills):

    for skill , value  in skills.items():

        print(f'Your skill is :')
        print(f'-{skill} => {value}%')

show_skill(**myskill)
#======================
tuple= ("python" , "html")

diction ={"css": 90 , 
          "java":84,
          "English":93}

def ditals(name,*skills,**skill_progras):

    print(f"Hello {name} your skill is ")

    for skill in skills :
        
        print(f"- {skill}")

    for keys , values in skill_progras.items():
        
        print(f'- {keys} --> {values}')
ditals("belal",*tuple , **diction)
#==========================
def clean_word(word):

    if len(word)==1:

        return word

    if word[0] == word[1]:

        return clean_word(word[1:])

    return word[0]+ clean_word(word[1:])

print(clean_word("wwwooooorrrlddd"))

def words(name):

    if len(name) == 1:

        return name

    if name[0] ==name[1]:

        return words(name[1:])

    return name[0] + words(name[1:])

print(words("bbbbbbbeeeeeelllllaalllll  waaaalllleeedd").title())
# =============================