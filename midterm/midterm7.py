def f(a, b):
	return (a + b)


def dict_interdiff(d1, d2):
	common_keys = list(set(d1.keys()) & set(d2.keys()))
	diff_keys = []
	for i in d1:
		if i not in common_keys:
			diff_keys.append(i)
	for i in d2:
		if i not in common_keys:
			diff_keys.append(i)

	res1 = {}

	res2 = {}

	for i in common_keys:
		res1[i] = f(d1[i], d2[i])
	j = 0		
	for i in diff_keys:
		if(i in d1):	
			res2[i] = d1[i]
 		else:
 			res2[i] = d2[i]

	result = []
	result.append(res1)
	result.append(res2)
	print(tuple(result))

d = {1:30, 2:20, 3:30, 5:80}
b = {1:40, 2:50, 3:60, 4:70, 6:90}

dict_interdiff(d, b)