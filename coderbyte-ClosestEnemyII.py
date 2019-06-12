'''
Challenge
Have the function ClosestEnemyII(strArr) read the matrix of numbers stored in strArr which will be a 2D matrix that contains only the integers 1, 0, or 2. Then from the position in the matrix where a 1 is, return the number of spaces either left, right, down, or up you must move to reach an enemy which is represented by a 2. You are able to wrap around one side of the matrix to the other as well. For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following: 

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2 

For this input your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 by moving left to wrap to the other side and then moving down once. The array will contain any number of 0's and 2's, but only a single 1. It may not contain any 2's at all as well, where in that case your program should return a 0. 

Sample Test Cases:

Input:["000", "100", "200"]
Output:1

Input:["0000", "2010", "0000", "2002"]
Output:2
'''

def ClosestEnemyII(array):
    enemies = []
    for i, row in enumerate(array):
        for j, col in enumerate(list(row)):
            if col == '1': px, py = (i, j)
            if col == '2': enemies.append((i, j))
    moves = []
    for x, y in enemies:
        no_wrap = abs(px - x) + abs(py - y)
        col_wrap, row_wrap = abs(px - x) + abs(py - (y - len(array))), abs(px - (x - len(array))) + abs(py-y)
        moves.append(min(no_wrap, col_wrap, row_wrap))
    return min(moves) if moves else 0
print ClosestEnemyII(raw_input())