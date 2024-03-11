from collections import deque

def solution(nums, k):
    answer = 0
    n = len(nums)

    for i in range(k):
        answer += nums[n-1-i]
        print
    temp = answer
    start = n-k

    for j in range(k):
        temp += nums[j]
        temp -= nums[start+j]

        answer = max(answer, temp)

    return answer
        
                                         
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))
