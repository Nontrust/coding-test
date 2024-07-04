def DFS(n):
    result = 1
    if n == 1:
        return result
    else:
        return n * DFS(n-1)

print(DFS(5))             
print(DFS(6))
print(DFS(7))
print(DFS(8))
