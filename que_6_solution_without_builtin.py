# Write a program (in Python, JavaScript or Ruby) to populate and then sort a
# randomly distributed list of 1 million integers, each integer having a value >= 1 and <=
# 100 without using any builtin/external library/function for sorting.
# Your program should carefully consider the input and come up with the most efficient
# sorting solution you can think of. Provide the space and time complexity of your algorithm

# Used Python for below solution
import timeit

setup = '''
import random 

# Function to generate 
# and append them  
# start_num = starting range, 
# end_num = ending range 
# range_num = number of  
# elements needs to be appended

def sorted_items(start_num, end_num, range_num):
 	list1 = []
 	list2 = []
 	for i in range(range_num):
 		#randint accepts two parameters, a lowest and a highest number
 		list1.append(random.randint(start_num, end_num))

 		while list1:
 			minimum = list1[0]
 			#iterating over list1
	 		for j in list1:
		 		if j < minimum:
		 			minimum = j

		 	list2.append(minimum)
		 	list1.remove(minimum)

		 			
		
 	return list2
   

print(sorted_items(start_num = 1, end_num = 100, range_num = 1000000))

'''

print (min(timeit.Timer(setup=setup).repeat(1)))



#Here I used the random module to create the list1 and iterated over list and put the lowest value members 
#into a new list list2 and removed them out of the old list list1. rinse and repeat until old list is empty.

#'timeit' module can be used to find out how long each takes...
#It takes 0.01133229999999985 for above example

# Space:
#----------

# memory taken by an algorithm to run as a function of the length of the input

# Time Complexity - Linear Time — O(n)
#-------------------------------------

# An algorithm is said to have a linear time complexity when the running time increases at most 
# linearly with the size of the input data. This is the best possible time complexity when the algorithm must 
# examine all values in the input data

