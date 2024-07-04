def solution2(nums):
    answer = -1
    for i, num in enumerate(nums):
        if (num == i):
            return i
    
    return answer

def solution(nums):
    lt, rt = 0, len(nums) -1
    while rt >= lt:
        mid = (rt+lt)//2
        if(nums[mid] == mid):
            return nums[mid]
        elif(nums[mid] < mid):
            lt = mid +1
        else:
            rt = mid - 1

    return -1
    
print(solution([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
print(solution([-10, -5, -2, 3, 4, 6, 7, 8]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution([-5, -3, 0, 1, 2, 3, 4, 7]))
print(solution([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  
