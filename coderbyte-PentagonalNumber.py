'''
Have the function PentagonalNumber(num) read num which will be a positive integer and determine how many dots exist in a pentagonal shape around a center dot on the Nth iteration. For example, in the image below you can see that on the first iteration there is only a single dot, on the second iteration there are 6 dots, on the third there are 16 dots, and on the fourth there are 31 dots. 

![image](https://i.imgur.com/fYj3yvL.png)

Your program should return the number of dots that exist in the whole pentagon on the Nth iteration. 

Hard challenges are worth 15 points and you are not timed for them. Use the Parameter Testing feature in the box below to test your code with different arguments.

Sample test case:

input: 2
output: 6

input: 5
output: 51
'''

def PentagonalNumber(num): 
    if num == 1:
        return 1
    else:
        return (num-1)*5 + PentagonalNumber(num-1)

    
# keep this function call here  
print PentagonalNumber(raw_input())  