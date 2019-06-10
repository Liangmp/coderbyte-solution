'''
Challenge
Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 
Sample Test Cases

Input:"coderbyte"

Output:etybredoc


Input:"I Love Code"

Output:edoC evoL I
'''

def FirstReverse(str): 
    lenStr = len(str)
    revert = ""
    for i in range(lenStr):
        revert = revert + str[lenStr-i-1]
    # code goes here 
    str = revert
    return str
    
# keep this function call here  
str = input()
print(FirstReverse(str)