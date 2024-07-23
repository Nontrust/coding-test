from collections import deque



def solution(home):
    answer = bfs(home)
    
    return answer

def bfs(home):
    L = 0
    check = [True] * 10001
    check[0] = False

    Q = deque()
    Q.append(0)

    while Q:
        n = len(Q)
        for i in range(n):
            x = Q.popleft()
            if x == home:
                return L
            for nx in [x-1, x+1, x+5]:
                if nx >= 0 and nx <= 10000 and check[nx]:
                    Q.append(nx)
                    check[nx] = False
        L += 1
            
print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))
