
s = 'azcbobobegghakl'

max_length = 0
curent_sub = s[0]
long_sub = s[0]

for i in range(len(s) - 1):
	if(s[i + 1] >= s[i]):
		curent_sub += s[i + 1]
		if(len(curent_sub) > max_length):
			max_length = len(curent_sub)
			long_sub  = curent_sub
	else:
		curent_sub = s[i + 1]

print ('Longest substring in alphabetical order is: ' + long_sub)