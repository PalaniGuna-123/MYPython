car ={
    "brand":"Tesla",
    "model":"model 3",
    "year": 2024
}
car2=dict(brand="Tesla",model="Model 3")
print(car)
print(car2)
print(len(car))
print(type(car2))

#Access items

print(car["brand"])
print(car.get("model"))

#list all keys
print(car.keys())
print(car.values())
print(car.items())     #output namakku tuple aaga kidaikkum

#verify key exits
print("model" in car)
print("mo" in car)

#change values
car["brand"]="Nio"
car.update({"price": 100000})
print("")
print(car)

#romove items
print(car.pop("price"))
print("")
print(car)
car["Ev"]="yes"
print(car)
print(car.popitem())  #tuple aaga return pannum
print(car)

#delete and clear
print("")
car["Ev"]="yes"
del car["Ev"]
print(car)
car2.clear()
print(car2)

del car2 

#copy dictionaries
car2=car.copy()
car2["Ev"]="No"
print("")
print("good copy")
print(car)
print(car2)

car3=dict(car)
print('')
print(car3)

#Nested dict
member1 = {
"name": "Plant",
"instrument": "brand"
}
member2 = {
"name": "Page",
"instrument": "model"
}
band = {
"member1": member1,
"member2": member2
}
print('')
print (band)
print (band ["member1"]["name"])
