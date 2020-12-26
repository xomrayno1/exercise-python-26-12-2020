def removeKey(person,keyToRemove):
    for key in keyToRemove:
        person.pop(key,None)
    return person

person = {
    "name" : "Quoc Nam",
    "age" : 28,
    "salary" : 8000,
    "city" : "Tuy Hoa"
}

keyToRemove = ["salary" , "city"]

newPerson = removeKey(person,keyToRemove)

print(newPerson)
