'''https://www.acmicpc.net/problem/1325   
효율적인 해킹
문제
 N개의 컴퓨터로 이루어져 있는 회사의 컴퓨터는 신뢰O, 신뢰X 관계로 이루어져 있는데, 
 A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹
 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. 
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, 
"A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

 
1 → 3→4↴
2 ↗  ↘5
 
출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

예제 입력 1 
5 4
3 1
3 2
4 3
5 3
예제 출력 1 
1 2
'''

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
maxV, res = -1, []

for _ in range(m):
    a, b = map(int, input().split())
    lst[b].append(a)

for i in range(1, n+1):
    visit = [0] * (n+1)
    if lst[i]:
        cnt = 1
        visit[i] = 1
        stack = [i]

        while stack:
            sti = stack.pop()
            for j in lst[sti]:
                if not visit[j]:
                    visit[j] = 1
                    cnt += 1
                    stack.append(j)

        if maxV < cnt:
            maxV = cnt
            temp = [i]
        elif maxV == cnt:
            temp.append(i)

print(*temp)