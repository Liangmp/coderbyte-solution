'''
Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol. So the string to the left would be false. The string will not be empty and will have at least one letter. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
'''

def SimpleSymbols(str): 
    str = '=' + str + '='
    for c in str:
        if c.isalpha():
            if not str[str.index(c)-1] == '+' or not str[str.index(c)+1] == '+':
                return 'false'
    return 'true'
    
# keep this function call here  
print SimpleSymbols(raw_input())