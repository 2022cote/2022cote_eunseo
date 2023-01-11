from collections import deque
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, l, r = map(int, input().split())  # n*n, 인구차이 l명 이상, r명 이하

arr = [list(map(int, input().split())) for i in range(n)]
a_list = list()
 