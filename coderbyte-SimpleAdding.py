'''
Have the function SimpleAdding(num) add up all the numbers from 1 to num. For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number from 1 to 1000. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
'''

def SimpleAdding(num): 
    sum = num
    for i in range(num):
        sum += i
    return sum
    
# keep this function call here  
print SimpleAdding(raw_input())