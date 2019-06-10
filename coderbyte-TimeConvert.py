'''
Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon. 

Use the Parameter Testing feature in the box below to test your code with different arguments.
'''

def TimeConvert(num): 
    hour = int(num/60)
    min = num - hour * 60
    # code goes here 
    return str(hour) + ':' + str(min)
    
# keep this function call here  
print TimeConvert(raw_input())