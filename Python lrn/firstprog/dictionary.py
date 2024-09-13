# Dictionary is nothing but key value pairs
d1 = {}
print(type(d1))
a={"Arindam":"Burger",
      "Sarthak":"Chicken",
      "Samrat":"Biriyani",
      "Deep":{"Breakfast":"maggie", "Lunch":"roti", "Dinner":"Rice"}}
a["joydeep"]="momo"
a[420]="kebabs"
print(a)
del a[420]
print(a["Deep"]["Breakfast"])
b = a.copy()
del b["Deep"]
print(b)
print(a)
a.update({"Zee":"Pizza"})
print(a.keys())
print(a.values())
print(a.items())