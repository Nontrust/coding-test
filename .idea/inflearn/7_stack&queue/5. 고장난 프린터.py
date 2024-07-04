from collections import deque
def solution(nums):
    queue = deque(nums)
    temp = 0
    while queue:
        if len(queue) == 1:
            return queue.pop()
        elif temp == 2:
            temp = 0
            left = queue.popleft()
            queue.append(left)
        else:
            temp += 1
            queue.popleft()
    return queue

def solution1(nums):
    queue =deque(nums)
    while queue:
        for _ in range(2):
            if len(queue)>=2:
                queue.popleft()
        queue.append(queue.popleft())
        if len(queue)==1:
            return queue[0]


print(solution1([3, 1, 4, 5, 2, 6, 7]))
print(solution1([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution1([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution1([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution1([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))
