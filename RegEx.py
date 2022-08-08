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

