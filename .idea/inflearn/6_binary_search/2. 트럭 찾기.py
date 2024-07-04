# from bisect import bisect_left
#
# def solution(nums, weight):
#     answer = bisect_left(nums, weight)
#     return answer if answer == len(nums) else -1


def solution2(nums, weight):
    lt, rt = 0, len(nums)
    nums = sorted(nums)
    while rt > lt:
        mid = (rt + lt) //2
        if(nums[mid] < weight):
            lt = mid +1
        else:
            rt = mid


    return -1 if rt == len(nums) else rt

    
     
print(solution2([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))
print(solution2([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
print(solution2([50, 55, 60, 65, 70, 80, 80, 80, 80, 90, 90, 90], 80))
print(solution2([20, 30, 40, 50, 60, 70], 90))
print(solution2([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))
