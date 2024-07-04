from collections import deque
def solution(s):
    queue = deque()
    for j in s:
        if len(queue)==0:
            queue.append(j)
        elif queue[-1] == j:
            queue.pop()
        else:
            queue.append(j)


    return "".join(queue)

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))
