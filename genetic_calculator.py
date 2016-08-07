import random 
import numpy as np
import bisect

f = [x for x in range(30000)]
m = [x for x in range(30000,60000)]


n=0

def new_person():
	global n
	l = []
	for i in range(n, n + 30000):
		l.append(i)
	n = n+30000
	return l

def kids_genetic_info(dad, mom):
	l = []
	for i in range(30000):
		p = random.random()
		if (p<=0.5):
			l.append(dad[i])
		else:
			l.append(mom[i])
	return np.sort(l)

def percent_in_common(person1, person2):
	simulation_times = 5
	n = 0
	for i in range(0,simulation_times):
		common = 0;
		for i in range(30000):
			j = index(person2, person1[i])
			if j is not -1:
				common = common + 1
		n = n + (common*100)/30000
	return n/simulation_times

def index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

#Example
#grandma  |
#grandpha |___mom's sister
#         |___mom |
#             dad |___ me

           
grandma = new_person()
grandpha = new_person()
mom = kids_genetic_info(grandma, grandpha)
dad = new_person()
moms_sister = kids_genetic_info(grandma, grandpha)
me = kids_genetic_info(mom, dad)

print(percent_in_common(mom, me))
print(percent_in_common(dad, me))
print(percent_in_common(moms_sister, me))
