def deep_reverse(L):
	L.reverse()
	for i in range(len(L)):
		j = i
		L[i].reverse()
	return L

L = [[1,2],[3, 4], [5,6, 7]]

deep_reverse(L)