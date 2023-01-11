
'''https://www.acmicpc.net/problem/2667	    단지번호붙이기		
'''
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(i, j):
    graph[i][j] = 0
    cnt = 1
    for k in range(4):
      x = i + dx[k]
      y = j + dy[k]
      if 0 <= x and x < N and 0 <= y and y < N:
        if graph[x][y] == 1:
            cnt += DFS(x, y)
    return cnt

num = 0
complexes = []
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            complexes.append(DFS(i, j))
            num += 1


print(num)
print(*sorted(complexes),sep='\n')