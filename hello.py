print("hello")
print("good day")

a=1
if a>3:
    print("Its large")
else :
    print('It is not a large')

multiline=(''' 
naan kandippa problem   
           solving la good marks score pannuven idhu sathiyam
''')
print (multiline)

sentence=("I AM A \" DOCTOR \t GUNA \n Guna is a gentle man")
print(sentence)
print(sentence.lower())
print(sentence.title())
print(sentence.upper())

print(len(sentence))
sentence+='              '
print(len(sentence))
sentence="      "+sentence
print(len(sentence))
print(len(sentence.strip()))
print(len(sentence.lstrip()))
print(len(sentence.rstrip()))

str="Guna"
print(str[0:4])
print(str.startswith("G"))
print(str.endswith("a"))
