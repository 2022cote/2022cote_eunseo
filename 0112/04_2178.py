'''https://www.acmicpc.net/problem/2178	    미로 탐색		
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)

'''
n,m=map(int,input().split())

d = [list(map(int, input())) for _ in range(n)]

di=[1,-1,0,0]
dj=[0,0,1,-1]
p=[]
c=0


p.append([0,0])

while c!=len(p):
    x=p[c][0]
    y=p[c][1]
    for i in range(4):
        dx=x+di[i]
        dy=y+dj[i]
        if dx>=0 and dx<n and dy>=0 and dy<m:
            if d[dx][dy]==1:
                p.append([dx,dy])
                d[dx][dy]=d[x][y]+1
    if d[n-1][m-1]!=1:
        break
    c+=1

print(d[n-1][m-1])