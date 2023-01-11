'''https://www.acmicpc.net/problem/7576	    토마토		
'''
 
from collections import deque
col,row  = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(row)]

Q=deque()
move=[[0,-1],[0,1],[-1,0],[1,0]]#상하좌우
for i in range(row):
    for j in range(col):
        if(arr[i][j] == 1):
            Q.append([i,j])

while(len(Q) != 0):
    r, c= Q.popleft()
    for i in move:
        m1=r+i[0]
        m2=c+i[1]   
        if(m1<0 or m1>row-1 or m2<0 or m2>col-1):
            continue
        elif(arr[m1][m2] == 0):
            arr[m1][m2]=arr[r][c]+1
            Q.append([m1,m2])
s=0
for i in range(row):
    for j in range(col):
        if(arr[i][j] == 0):
            print(-1)
            exit(0)
        if(s<(arr[i][j]-1)):
            s=arr[i][j]-1
print(s)