mytuple=tuple(("john",43,True))
anothertuple=(1,6,8,9,5,3,22,2,2)
print(mytuple)
print(type(mytuple))
print(anothertuple)  #tupleyai eppavume maatrave mudiyaadhu
newlist=list(mytuple)
newlist.append("Henry")
print(newlist)
newtuple=tuple(newlist)
print(newtuple)
(one,*two,hey)=anothertuple
print(one)
print(two)
print(hey)
print(anothertuple.count(2))
