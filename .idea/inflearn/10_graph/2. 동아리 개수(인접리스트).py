def solution(n, edges):
    check = [False] * (n+1)
    graph = [[] for _ in range(n+1)]

    for [a, b] in edges:
        graph[a].append(b)
        graph[b].append(a)
    answer = 0

    for i in range(1, n+1):
        if not check[i]:
            answer += 1
            dfs(i, graph, check, n)

    return answer

def dfs(node, graph, check, n):
    check[node] = True
    for n in graph[node]:
        if not check[n]:
            dfs(n, graph, check, n)

                    


print(solution(10, [[1, 2], [2, 3], [1, 4], [1, 5], [6, 8], [7, 8], [9, 10]]))
print(solution(20, [[1, 2], [2, 5], [5, 7], [9, 7], [5, 13], [15, 13], [3, 4], [4, 6], [6, 8], [8, 10], [11, 12], [14, 16], [16, 17], [17, 18], [19, 20]]))
print(solution(7, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
print(solution(30, [[5, 6], [6, 7]]))

