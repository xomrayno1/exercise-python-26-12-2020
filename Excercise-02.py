def convertToDict(list1,list2):
    
    newDict = {list1[i] : list2[i]  for i in  range(0,len(list1))}
    return newDict

list1 =['A','B','C','D','E','F']
list2 = [1,2,3,4,5,6]

newDict  =  convertToDict(list1,list2)

print(newDict)