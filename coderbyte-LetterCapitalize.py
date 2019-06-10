'''
Have the function LetterCapitalize(str) take the str parameter being passed and capitalize the first letter of each word. Words will be separated by only one space. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
'''

def LetterCapitalize(str): 

    list = str.split(" ")
    newStr = ""
    for word in list:
        newStr += word[0].upper()
        for i in range(1, len(word)):
            newStr += word[i]
        newStr += " "
    newStr = newStr[:-1]
    return newStr
    
# keep this function call here  
print LetterCapitalize(raw_input())