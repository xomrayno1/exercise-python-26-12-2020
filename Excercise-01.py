def getNewListA(listA):
    while 10 in listA:
        listA.remove(10)
    return listA

listA  = [1,10,20,5,60,30,10,9,10]

newListA = getNewListA(listA)
print(newListA)
 
