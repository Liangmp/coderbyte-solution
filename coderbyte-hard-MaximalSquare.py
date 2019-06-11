'''
Challenge (hard)

Have the function MaximalSquare(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's, and determine the area of the largest square submatrix that contains all 1's. A square submatrix is one of equal width and height, and your program should return the area of the largest submatrix that contains only 1's. For example: if strArr is ["10100", "10111", "11111", "10010"] then this looks like the following matrix: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0 

For the input above, you can see the bolded 1's create the largest square submatrix of size 2x2, so your program should return the area which is 4. You can assume the input will not be empty. 

Hard challenges are worth 15 points and you are not timed for them.

Sample Test Cases

Input:["0111", "1111", "1111", "1111"]

Output:9

Input:["0111", "1101", "0111"]

Output:1
'''
def MaximalSquare(strArr):
    l = list([[int(x) for x in s] for s in strArr])
    row = len(strArr)
    col = len(strArr[0])
    F = min(row, col)
    
    for f in range(F, 0, -1):  # descending searching
        for i in range(0, row-f+1):    # from row to row (filter goes from upper to bottom)   
            # if f == row, do this for loop only once
            # i is the row index of the matrix
            for j in range(0, col-f+1): # from column to column (filter goes from left to right)
                # if f == col, do this loop only once
                # j is the column index of the matrix
                # strArr[i][j] is the upper left corner of the submatrix
                multiply = 1
                
                # l[m][n] is the elements of the submatrix
                for m in range(i, f+i):
                    for n in range(j, f+j):
                        multiply *= l[m][n]
                ## after all the multiply operator:
                if multiply == 1:
                    return f*f
    return 0
    
print MaximalSquare(raw_input())