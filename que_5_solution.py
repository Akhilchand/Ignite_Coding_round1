# Question 5.

# Consider the following pattern:

# A → D M → P X → A
# a → d m → p x → a

# Now, write a program to solve the following message using Python, JavaScript or Ruby.
# Vrphwklqj phdqlqjixo
# Hint: The answer is something meaningful.

# Used Python for below solution

""" To Map A -> D, m ->p likewise
    String is string parameter
    String parameter can be string or para or word
"""
message='''Vrphwklqj phdqlqjixo'''
output=""
for i in range(0,len(message)):
	#for capital characters converting to ASCII
	if ord(message[i])>=65 and ord(message[i])<=90:
		shifted=ord(message[i])-3
		if shifted<65:
			shifted=shifted+26
		#converting ASCII back to character and assigning to output
		output=output+chr(shifted)
		continue
		#for lower characters converting to ASCII
	elif ord(message[i])>=97 and ord(message[i])<=122:
		shifted=ord(message[i])-3
		if shifted<97:
			shifted=shifted+26
		#converting ASCII back to character and assigning to output
		output=output+chr(shifted)
		continue
	else:
		output=output+message[i]
 
print(output)

# Output:
# --------
# Output:   Something meaningful