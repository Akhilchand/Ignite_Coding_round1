# Question 6. Python, Ruby or JavaScript

# Use the following paragraphs (in italics below) as input to the program you wrote for Question 5.
# It should output a meaningful question. Write a program to solve that question.
# Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw d
# udqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg <=
# 100 zlwkrxw xvlqj dqb exlowlq/hawhuqdo oleudub/ixqfwlrq iru vruwlqj.
# Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw
# vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu dojrulwkp

# Used Python for below solution

question='''Zulwh d surjudp (lq Sbwkrq, MdydVfulsw ru Uxeb) wr srsxodwh dqg wkhq vruw d
udqgrpob glvwulexwhg olvw ri 1 ploolrq lqwhjhuv, hdfk lqwhjhu kdylqj d ydoxh >= 1 dqg <=
100 zlwkrxw xvlqj dqb exlowlq/hawhuqdo oleudub/ixqfwlrq iru vruwlqj.
Brxu surjudp vkrxog fduhixoob frqvlghu wkh lqsxw dqg frph xs zlwk wkh prvw hiilflhqw
vruwlqj vroxwlrq brx fdq wklqn ri. Surylgh wkh vsdfh dqg wlph frpsohalwb ri brxu dojrulwkp'''
output=""
for i in range(0,len(question)):
	#for capital characters converting to ASCII
	if ord(question[i])>=65 and ord(question[i])<=90:
		shifted=ord(question[i])-3
		if shifted<65:
			shifted=shifted+26
		#converting ASCII back to character and assigning to output
		output=output+chr(shifted)
		continue
		#for lower characters converting to ASCII
	elif ord(question[i])>=97 and ord(question[i])<=122:
		shifted=ord(question[i])-3
		if shifted<97:
			shifted=shifted+26
		#converting ASCII back to character and assigning to output
		output=output+chr(shifted)
		continue
	else:
		output=output+question[i]
 
print(output)

# Output:
# ------
# Write a program (in Python, JavaScript or Ruby) to populate and then sort a
# randomly distributed list of 1 million integers, each integer having a value >= 1 and <=
# 100 without using any builtin/external library/function for sorting.
# Your program should carefully consider the input and come up with the most efficient
# sorting solution you can think of. Provide the space and time complexity of your algorithm