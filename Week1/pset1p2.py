
s = 'azcbobobegghakl'

sub = 'bob'
	
l = 0	
j = 0
count = 0
while(l < len(s)):
	if(s[l] == sub[j]):
		if(j == len(sub) - 1):
			count += 1
			j = 0
		l += 1
		j += 1
	else:
		l += 1
		j =0

print("Number of times bob occurs is: %d" % count)



count = 0
i = 0
j = 1
k = 2
while (k < len(s)):
    if s[i] == 'b' and s[j] == 'o' and s[k] == 'b':
        count += 1
    i += 1
    j += 1
    k += 1
print("Number of times bob occurs is: %d" % count)