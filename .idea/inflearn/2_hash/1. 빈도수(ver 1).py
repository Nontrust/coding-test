def solution(nums):
    dat = [0]*10000
    answer = -1
    for num in nums:
        dat[num] += 1
    for i in range(len(dat)):
        if dat[i] == 1 and answer < i :
            answer = i

    return answer
                            
                
print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))
