from collections import deque
def solution(s):
    queue = deque()
    for j in s:
        if(j=='('):
            queue.append(j)
        else:
            if(len(queue) ==0 ):
                return "NO"
            queue.pop()
    return "YES" if len(queue) == 0 else "NO"


print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))
