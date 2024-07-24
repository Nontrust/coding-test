from collections import deque

cnt = 0
def solution(n, edges):
    global cnt
    check = [False] * (n+1)

    graph = [[False] * (n+1) for _ in range(n+1)]
    for [a,b] in edges:
        graph[b][a] = True
        graph[a][b] = True
    cnt = 0

    dfs(1, graph, check, n)

    return n - cnt

def dfs(node, graph, check, n):
    global cnt
    check[node] = True
    cnt += 1
    for other in range(1, n+1):
        if graph[node][other] and not check[other]:
            dfs(other, graph, check, n)

print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))

