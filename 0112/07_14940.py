
'''https://www.acmicpc.net/problem/14940	쉬운 최단거리		
'''
from collections import deque
import copy

n,m=map(int,input().split())
dx,dy=[0,0,1,-1],[1,-1,0,0]
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            board[i][j]=-1
        if board[i][j]==2:
            tn,tm=i,j
            
board[tn][tm]=0

q=deque([(tn,tm)])
while q:
    nowX,nowY=q.popleft()
    for d in range(4):
        nextX,nextY=nowX+dx[d],nowY+dy[d]
        if nextX<0 or nextX>=n or nextY<0 or nextY>=m or board[nextX][nextY]!=-1:
            continue
        board[nextX][nextY]=board[nowX][nowY]+1
        q.append((nextX,nextY))
for arr in board:
    print(" ".join(list(map(str,arr))))