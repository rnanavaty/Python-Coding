# Regular expressions (RegEx) in action 

import re

text = 'FullString123ends'

# Example-1 : search function
print('\nOutput of example-1 is : ')
print(re.search('123', text))

# Example-2 : search function with meta-characters
print('\nOutput of example-2 is : ')
print(re.search('[0-9][0-9][0-9]', text))

# Example-3 search of first occurance in hyphen '-'
print('\nOutput of example-3 is : ')
print(re.search('[a-z]', text))
print(re.search('[0-9]', text))

# Example-4 search of first hexadecimal character
print('\nOutput of example-4 is : ')
print(re.search('[0-9a-fA-f]', '--- g6 ---'))

# Example-5 search of complement a character
print('\nOutput of example-5 is : ')
print(re.search('[^0-9]', '12345text'))

# Example-6 search of literal character '-' start, end and in-between
print('\nOutput of example-6 is : ')
print(re.search('[-abc]', '123-456'))
print(re.search('[abc-]', '123-456'))
print(re.search('[ab\-c]', '123-456'))

# Example-7 search of closing bracket ']'
print('\nOutput of example-7 is : ')
print(re.search('[]]', 'text[1]'))
print(re.search('[ab\]cd]', 'text[1]'))

# Example-8 dot (.) as wildcard character
# dot matches first occurance of single character except a newline
print('\nOutput of example-8 is : ')
print(re.search('right.speech', 'right2speech'))
print(re.search('right.speech', 'rightspeech'))
print(re.search('right.speech', 'right\vspeech'))
print(re.search('right.speech', 'right\nspeech'))

# Example-9 
# \w - matches first occurance of alphanumeric character
# \W - matches first occurance of Non-alphanumeric character
# Word characters are uppercase, lowercase letters, digits, 
# and the underscore (_)
print('\nOutput of example-9 is : ')
print(re.search('\w', '#(.a$@&'))
print(re.search('\W', 'This_is__@gmail.com'))

# Example-10
# \d - matches first occurance of digit
# \D - matches first occurance of Non-digit
print('\nOutput of example-10 is : ')
print(re.search('\d', 'right2speech'))
print(re.search('\D', '2345num123'))

# Example-11
# \s - matches 
# \S - matches any Non-digit
print('\nOutput of example-11 is : ')
print(re.search('\s', 'right\nspeech'))
print(re.search('\S', '   \n\v\snum123'))
print(re.search('[\d\w\s]', '--- ---'))

# Example-12 
print('\nOutput of example-12 is : ')
print(re.search('.', 'myemail@gmai.com'))
print(re.search('\.', 'myemail@gmai.com'))

#############################################################
Output
#############################################################
Output of example-1 is : 
<re.Match object; span=(10, 13), match='123'>

Output of example-2 is : 
<re.Match object; span=(10, 13), match='123'>

Output of example-3 is : 
<re.Match object; span=(1, 2), match='u'>
<re.Match object; span=(10, 11), match='1'>

Output of example-4 is : 
<re.Match object; span=(5, 6), match='6'>

Output of example-5 is : 
<re.Match object; span=(5, 6), match='t'>

Output of example-6 is : 
<re.Match object; span=(3, 4), match='-'>
<re.Match object; span=(3, 4), match='-'>
<re.Match object; span=(3, 4), match='-'>

Output of example-7 is : 
<re.Match object; span=(6, 7), match=']'>
<re.Match object; span=(6, 7), match=']'>

Output of example-8 is : 
<re.Match object; span=(0, 12), match='right2speech'>
None
<re.Match object; span=(0, 12), match='right\x0bspeech'>
None

Output of example-9 is : 
<re.Match object; span=(3, 4), match='a'>
<re.Match object; span=(9, 10), match='@'>

Output of example-10 is : 
<re.Match object; span=(5, 6), match='2'>
<re.Match object; span=(4, 5), match='n'>

Output of example-11 is : 
<re.Match object; span=(5, 6), match='\n'>
<re.Match object; span=(5, 6), match='\\'>
<re.Match object; span=(3, 4), match=' '>

Output of example-12 is : 
<re.Match object; span=(0, 1), match='m'>
<re.Match object; span=(12, 13), match='.'>
#############################################################



