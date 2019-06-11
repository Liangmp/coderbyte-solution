'''
Challenge (easy)

Have the function CorrectPath(str) read the str parameter being passed, which will represent the movements made in a 5x5 grid of cells starting from the top left position. The characters in the input string will be entirely composed of: r, l, u, d, ?. Each of the characters stand for the direction to take within the grid, for example: r = right, l = left, u = up, d = down. Your goal is to determine what characters the question marks should be in order for a path to be created to go from the top left of the grid all the way to the bottom right without touching previously travelled on cells in the grid. 

For example: if str is "r?d?drdd" then your program should output the final correct string that will allow a path to be formed from the top left of a 5x5 grid to the bottom right. For this input, your program should therefore return the string rrdrdrdd. There will only ever be one correct path and there will always be at least one question mark within the input string. 

Sample Test Cases:

Input:"???rrurdr?"
Output:dddrrurdrd


Input:"drdr??rrddd?"
Output:drdruurrdddd
'''

def CorrectPath(s): #bruteforce ftw!
	import random
	while True:
		route=[]
		tracepos=[]
		x=1;y=5;answer=1
		for i in s:
			if i=="?":i=random.choice("lrud")
			if i=="u":y+=1
			elif i=="d":y-=1
			elif i=="r":x+=1
			elif i=="l":x-=1
			if (x,y) in tracepos:
				answer=0
				break
			else: tracepos.append((x,y))
			route.append(i)
			if x==6 or x==0 or y==0 or y==6:
				answer=0
				break
		if x==5 and y==1 and answer==1:
			return "".join(route)

print CorrectPath(raw_input())