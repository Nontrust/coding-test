def solution(nums, target):
    lt, rt = 0, len(nums)-1
    while lt<=rt:
        mid = (lt+rt)//2
        if nums[mid]==target:
            return nums[mid]
        elif nums[mid]>target:
            rt=mid-1
        elif nums[mid]<target:
            lt=mid+1

    return -1
                                                 
print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))
