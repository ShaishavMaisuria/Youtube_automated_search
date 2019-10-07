def convertTheString(word):
    lists = word.split()
    newString=""
    for x in lists:
        newString += x + "+"

    newString = newString[:-1]

    return print(str(newString) +" new String")



newString =""
word = input()
convertTheString(word)


'''listt=[word]
lists = word.split()

for x in lists:
    newString+= x+ "+"

print(listt)
newString=newString[:-1]
print(str(newString) +" new String")
print(str(len(newString)) +" new String" +"\n")
print(str(len(word)) +" words")
print()'''


