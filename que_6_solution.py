# Write a program (in Python, JavaScript or Ruby) to populate and then sort a
# randomly distributed list of 1 million integers, each integer having a value >= 1 and <=
# 100 without using any builtin/external library/function for sorting.
# Your program should carefully consider the input and come up with the most efficient
# sorting solution you can think of. Provide the space and time complexity of your algorithm

# Used Python for below solution


import random 
import sys

# Function to generate 
# and append them  
# start_num = starting range, 
# end_num = ending range 
# range_num = number of  
# elements needs to be appended

def sorted_items(start_num, end_num, range_num):
	list1 = []
	for i in range(range_num):
		#randint accepts two parameters, a lowest and a highest number
		list1.append(random.randint(start_num, end_num))
		list1.sort() #sorting the items in the list
	
	return list1

file = open('output.txt', 'a') #opening a text file named output and appending output to it.
sys.stdout = file
print(sorted_items(start_num = 1, end_num = 100, range_num = 1000000))
file.close() #closing file


# Space:
#----------

# memory taken by an algorithm to run as a function of the length of the input

# Time Complexity - Linear Time — O(n)
#-------------------------------------

# An algorithm is said to have a linear time complexity when the running time increases at most 
# linearly with the size of the input data. This is the best possible time complexity when the algorithm must 
# examine all values in the input data

