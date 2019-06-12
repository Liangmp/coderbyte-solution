'''
Challenge

Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well. 

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string. 

Sample Test Cases

Input:"aa6?9"
Output:false

Input:"acc?7??sss?3rr1??????5"
Output:true
'''

def QuestionsMarks(s): 
    numbers = '1234567890'
    lastDigit = None
    answer = 'false'
    for i in range(0, len(s)):
        if s[i].isdigit():
            if lastDigit:
                if int(s[i]) + int(s[lastDigit]) == 10:
                    if s[lastDigit:i].count('?') == 3:
                        answer = 'true'
                    else:
                        return 'false'
            lastDigit = i
    
    return answer
    
# keep this function call here  
print QuestionsMarks(raw_input())  