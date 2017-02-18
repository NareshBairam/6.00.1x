
def flatten(aList): 
    res = [] 
    for el in aList: 
        if isinstance(el,list): 
            res.extend(flatten(el))     
        else: 
            res.append(el) 
    return res 

def flatten2(aList):
	bList = aList[:]
	for i in bList:
		if(type(i) == type([])):
			aList.remove(i)
			flatten(i)
		else:
			aList.append(i)
	return aList	

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
aList =  flatten(aList)
print(aList)