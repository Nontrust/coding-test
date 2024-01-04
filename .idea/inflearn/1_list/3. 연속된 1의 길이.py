def solution(nums):
    answer, temp = 0, 0
    for num in nums:
        if num == 1:
            temp += 1
            answer = max(temp, answer)
        else:
            temp = 0
    
    return answer

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
