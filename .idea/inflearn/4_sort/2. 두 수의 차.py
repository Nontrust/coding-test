def solution(nums):
    answer = []
    min = 999999
    nums.sort()
    for i in range(1, len(nums)):
        t = nums[i] - nums[i-1]
        if min == t:
            answer.append([nums[i-1], nums[i]])
        elif min > t:
            answer = [[nums[i-1], nums[i]]]
            min = t

                
    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))
