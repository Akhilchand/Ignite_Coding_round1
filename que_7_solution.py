# Question 7.

# Write a simple program that reads a line from the keyboard and outputs the same line where
# every word is reversed. A word is defined as a continuous sequence of alphanumeric characters
# or hyphen (‘-’). For instance, if the input is

# “We are at Ignite Solutions! Their email-id is careers@ignitesol.com”
# the output should be
# “eW era ta etingI snoituloS! riehT di-liame si sreerac@losetingi.moc”
# HINT: ​Read the problem and the example carefully before starting.

# Used Python for below solution


#re is regular expression library in Python
import re
str1 = input("enter the string: ")
#Using re library which has sub function re.sub(pattern, repl, string, count=0, flags=0)
#[\-a-z]+ is the regular expression for a positive sequence of hyphen, lower and upper case letters
#lambda x: x.group(0)[::-1] is used to reverse each word in the string
str2 = re.sub(r'[\-a-zA-Z]+', lambda x: x.group(0)[::-1], str1)
print(str2)
