def closest_power(base, num):
	min  = 0
	for i in range(int(num)):
		before = base**i
		after = base**(i + 1)
		if before <= num and after >= num:
			
			if(abs(before - num) <= (abs(after - num))):
				min = i
			else:
				min = i + 1
	return min

closest_power(4, 1) 

