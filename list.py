grocery=["apple","Banana","Grapes","Potato"]
family=["Guna","Sridhar","Gomathi","Palani"]
print("appl3e" in grocery)
print(grocery[-1])
print(grocery[-3])
print(grocery.index("apple"))
print(grocery[0:4])
print(len(grocery))
grocery.append('orage')
print(grocery)
grocery+=["rice"]
print(grocery)
grocery.extend(["fish","chiken"])
print(grocery)
grocery.extend(family)
print(grocery)
grocery.insert(0,"mutton") #first la add panna idhu use aagum 
print(grocery)
print('')
grocery[2:2]=["pepper","onion"]  #inga insert nadakkum
print(grocery)
print('')
grocery[1:3]=["chilli","tomato"]  #inga replacement nadakkum
print(grocery)
print('')
grocery.remove('Guna')
print(grocery)
print('')
print(grocery.pop())
print(grocery)
print('')
del grocery[0]
print(grocery)
print('')
family.clear()
print(grocery)
print('')
grocery.sort()
print(grocery)
print("")
grocery[1:2]=["salt"]
grocery.sort()
print(grocery)
print("")
grocery.sort(key=str.lower)
print(grocery)

nums =[2,3,4,5,77,3]
nums.reverse()
print(nums)

nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

nums =[1,24,35,67,3,5]
print(sorted(nums,reverse=True))
print(nums)

numscopy=nums.copy()
mynums=list(nums)
mycopy=nums[:]
print("")
print(mynums)
print(numscopy)
print(mycopy)

mylist=list([1,"Guna",True])
print(mylist)
print(type(mylist))

