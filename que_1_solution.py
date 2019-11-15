# Question 1. Python, Ruby or JavaScript
# Write a function that takes an array of integers and returns that array rotated by N positions
# using Python or Ruby or JavaScript.
# For example, if N=2, given the input array [1, 2, 3, 4, 5, 6]
# the function should return [5, 6, 1, 2, 3, 4]

# Used Python for below solution


def rotated_array(array_of_int, n):  # n = no of times array to be rotated
    n = int(input("enter value for n: "))  # user input for n rotations
    array_of_int = (array_of_int[-n:] + array_of_int[:-n])
    return(array_of_int)


print(rotated_array(array_of_int=[1, 2, 3, 4, 5, 6], n=2))
