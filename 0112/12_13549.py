from collections import deque

n, k = map(int, input().split())  # n: 수빈 , k: 동생
q = deque()
q.append(n) 
visited = [-1 for _ in range(100001)]
visited[n] = 0