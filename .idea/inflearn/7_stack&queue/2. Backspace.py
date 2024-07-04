from collections import deque
def solution(s):
    answer = ""
    queue = deque()
    for j in s:
        if(j == "#"):
            queue.pop()
        else:
            queue.append(j)
    return "".join(queue)
            
          
print(solution("abc##ec#ab"))
print(solution("kefd#ef##s##"))
print(solution("teac#cher##er"))
print(solution("englitk##shabcde##ff##ef##ashe####"))
print(solution("itistime####gold"))
