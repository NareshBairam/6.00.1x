def dotProduct(listA, listB):
	ProductSum = 0
	for i in range(len(listA)):
		ProductSum += listA[i]*listB[i]
	return ProductSum


listA = [1,2,3]
listB = [4,5,6]
p = dotProduct(listA, listB)
print(p)