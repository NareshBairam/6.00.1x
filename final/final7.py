def general_poly(L):
	l = len(L) - 1
	x = 10
	n = 0
    while(l >= 0):
		n = (L[i]*(x**l) + n)
		l -= 1
    return n


print(general_poly([1, 2, 3, 4]))