'''
Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
'''

import re

def LongestWord(sen): 
    list = sen.split(" ")
    longest = re.sub(r'[^a-zA-Z0-9]',"", list[0])
    for word in list:
        word = re.sub(r'[^a-zA-Z0-9]',"", word)
        if len(word) > len(longest):
            longest = word
    return longest
    
# keep this function call here  
str = input()
print(LongestWord(str))