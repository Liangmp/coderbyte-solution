'''
Challenge

Have the function ScaleBalancing(strArr) read strArr which will contain two elements, the first being the two positive integer weights on a balance scale (left and right sides) and the second element being a list of available weights as positive integers. Your goal is to determine if you can balance the scale by using the least amount of weights from the list, but using at most only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means there is a balance scale with a weight of 5 on the left side and 9 on the right side. It is in fact possible to balance this scale by adding a 6 to the left side from the list of weights and adding a 2 to the right side. Both scales will now equal 11 and they are perfectly balanced. Your program should return a comma separated string of the weights that were used from the list in ascending order, so for this example your program should return the string 2,6 

There will only ever be one unique solution and the list of available weights will not be empty. It is also possible to add two weights to only one side of the scale to balance it. If it is not possible to balance the scale then your program should return the string not possible. 

Sample Test Cases:

Input:["[3, 4]", "[1, 2, 7, 7]"]
Output:"1"


Input:["[13, 4]", "[1, 2, 3, 6, 14]"]
Output:"3,6"
'''

import itertools

def ScaleBalancing(strArr): 
    x = list(int(s) for s in strArr[0][1:-1].split(','))
    y = list(int(s) for s in strArr[1][1:-1].split(','))
    # one
    for a in y:
        if x[0] + a == x[1] or x[1] + a == x[0]:
            return str(a)
    # two
    for pair in itertools.combinations(y, 2):
        if x[0] + pair[0] == x[1] + pair[1] or x[0] + pair[1] == x[1] + pair[0] or x[0] + pair[0] + pair[1] == x[1] or x[1] + pair[0] + pair[1] == x[0]:
            return ''.join(str(min(pair)) + ',' + str(max(pair)))
    
    return "not possible"
    
# keep this function call here  
print ScaleBalancing(raw_input())  