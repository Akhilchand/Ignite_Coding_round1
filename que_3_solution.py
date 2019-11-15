# Question 3. Python, Ruby or JavaScript
# Most languages have a built in sort method that will sort an array of strings alphabetically.
# Demonstrate how to sort an array of strings by the length of each string, shortest strings first.
# Hint: clean, small code wins.

# Used Python for below solution

items = ['abcde', 'abcd', 'abc', 'abcdefg']
# The key parameter takes a function as its value, which is applied to each element before sorting, so that
# the elements are sorted based on the output of this function.
sorted_items = sorted(items, key=len) 
# sorted is used to sort string or int in ascending or descending order based on requirement
print(sorted_items)