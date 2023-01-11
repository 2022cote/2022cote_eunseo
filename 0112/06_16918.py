
'''https://www.acmicpc.net/problem/16918	봄버맨		
'''
#크기가 R×C인 직사각형 , N초 후
from collections import deque
 
R, C, N = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]   # 폭탄 설치

bombs = [ [r,c]   for r in range(R) for c in range(C) if arr[r][c] == 'O']   # 폭탄의 위치
bomb3 = [['O']*C for _ in range(R)]    # 4xi+3초 후 
bomb1 = [['O']*C for _ in range(R)]    # 4xi+1초 후 

li =[(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

# N이 짝수인 경우
if N % 2 == 0:
    for i in range(R): print("O" * C)  

elif N == 1:
    for x in arr: print("".join(x))

else:
    # 초기 폭탄 폭발
    for b in bombs:
        for di, dj in li:
            ni = b[0] + di
            nj = b[1] + dj
            if 0<=ni<R and 0<=nj<C:
                bomb3[ni][nj] = '.'

    bomb = []
    # 폭발 후 남은 폭탄의 위치
    for r in range(R):
        for c in range(C):
            if bomb3[r][c] == 'O':
                bomb.append([r, c])

    # 폭탄 폭발
    for b in bomb:
        for di, dj in li:
            ni = b[0] + di
            nj = b[1] + dj
            if 0 <= ni < R and 0 <= nj < C:
                bomb1[ni][nj] = '.'

    if N % 4 == 3:
        for r in range(R):
            print(*bomb3[r], sep='')
    else:   # 나머지가 1인 경우
        for r in range(R):
            print(*bomb1[r], sep='')