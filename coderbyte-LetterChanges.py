### coderbyte

'''
Challenge
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 
Sample Test Cases


Input:"hello*3"

Output:Ifmmp*3


Input:"fun times!"

Output:gvO Ujnft!

'''

def LetterChanges(str): 
    letterList = "abcdefghijklmnopqrstuvwxyz"
    vowelList = "aeiou"
    str = str.lower()
    newStr = ""
    
    # to the next letter
    for i in range(len(str)):
        if str[i].isalpha():
            index = letterList.find(str[i])
            letter = letterList[index+1]
            if vowelList.find(letter) != -1:
                letter = letter.upper()
            newStr = newStr + letter
        else:
            newStr = newStr + str[i]
        
    str = newStr
    return str
    
# keep this function call here  
str = input()
#letterList = "abcdefghijklmnopqrstuvwxyz"
#print(letterList.find("a"))
print(LetterChanges(str))