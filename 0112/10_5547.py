
'''https://www.acmicpc.net/problem/5547	    일루미네이션		
'''
from collections import deque

w, h = map(int, input().split())

wall = [[0]*(w+2) for _ in range(h+2)]

for i in range(1, h+1): 
    wall[i][1:w+1]=map(int, input().split())

dx = [-1,-1,0,0,1,1]
dy=[[0,1,-1,1,0,1],[-1,0,-1,1,-1,0]]

result = 0
queue = deque([])
visited = [[0] * (w + 2) for _ in range(h + 2)]
queue.append((0, 0))
visited[0][0] = True

while queue:
    x, y = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[x%2][i]
         
        if 0<=nx<h+2 and 0<=ny<w+2:
            if wall[nx][ny]==0 and not visited[nx][ny]: 
                visited[nx][ny]=1
                queue.append((nx, ny))
            elif wall[nx][ny]==1: 
                result+=1
print(result)