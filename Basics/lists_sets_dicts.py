#================List==============

d = ["belal waleed ahmed"]
e = ["mohamed"]

d.extend(e)
print(d)
d.append(e)
print(d)
d.reverse()
print(d)

print("=" * 50)

# ===================== Dictionary =====================

user = {
    "name": "belal",
    "age": 16,
    "country": "Egypt",
    "skill": "python",
    "level": "legendry"
}

print(user)
print(user["name"])
print(user.values())
print(user.keys())
print("=" * 50)

language = {
    "first": {"name": "english", "level": "b2"},
    "second": {"name": "python", "level": "50%"},
    "third": {"name": "arabic", "level": "90%"}
}

print(language)
print(language.values())
print(language.keys())
print(language["second"]["name"])
print(len(language["second"]))
print("=" * 50)

all = {"one": user, "two": language}

print(all)
print(all.values())
print(all.keys())
print(all["two"]["second"]["name"])
print(len(all["one"]))
print("=" * 50)

print(user)
print(user.setdefault("last name", "waleed"))
print(user)

print("=" * 50)

# ===================== List =====================

d = ["belal waleed ahmed"]
e = ["mohamed"]

d.extend(e)
print(d)
d.append(e)
print(d)
d.reverse()
print(d)

print("=" * 50)