'''
Challenge
Have the function EightQueens(strArr) read strArr which will be an array consisting of the locations of eight Queens on a standard 8x8 chess board with no other pieces on the board. The structure of strArr will be the following: ["(x,y)", "(x,y)", ...] where (x,y) represents the position of the current queen on the chessboard (x and y will both range from 1 to 8 where 1,1 is the bottom-left of the chessboard and 8,8 is the top-right). Your program should determine if all of the queens are placed in such a way where none of them are attacking each other. If this is true for the given input, return the string true otherwise return the first queen in the list that is attacking another piece in the same format it was provided. 

For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true. The corresponding chessboard of queens for this input is below (taken from Wikipedia). 

![](https://i.imgur.com/zAT24ML.png)
 
Sample Test Cases:

Input:["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]

Output:"(2,1)"


Input:["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]

Output:"(5,3)"
'''

def EightQueens(strArr): 
    x = list([[int(i) for i in p[1:-1].split(',')[0]] for p in strArr])
    y = list([[int(i) for i in p[1:-1].split(',')[1]] for p in strArr])
    #queenList = list([ [int(i) for i in p[1:-1].split(',')[0], int(j) for j in p[1:-1].split(',')[1]] for p in strArr ])
    queenList = []
    for i in range(0,len(x)):
        queenList.append((x[i][0],y[i][0]))

    for i in range(0, len(x)-1):
        for j in range(i+1, len(x)):
            x1, y1 = queenList[i]
            x2, y2 = queenList[j]
            if x1 == x2 or y1 == y2 or (x1 == y2 and x2 == y1) or x1 - y1 == x2 - y2:
                return '(' + str(x1) + ',' + str(y1) + ')'
    return 'true'
    
# keep this function call here  
print EightQueens(raw_input())