from collections import Counter, defaultdict
def solution2(nums):
    answer = 0
    num_counter = Counter(nums)
    for num in num_counter:
        if num == num_counter[num]:
            return num

    return -1

def solution(nums):
    nums_dict = defaultdict(int)
    for num in nums:
         nums_dict[num] += 1
    print(nums_dict)

    for n in nums_dict:
        if nums_dict[n] == n:
            return n
    return -1


print(solution([1, 2, 3, 1, 3, 3, 2, 4]))
print(solution([1, 2, 3, 3, 3, 2, 4, 5, 5, 5]))
print(solution([1, 1, 2, 5, 5, 5, 5, 5, 3, 3, 3, 3, 5]))
print(solution([7, 6, 7, 7, 8, 8, 8, 8, 7, 5, 7, 7, 7, 8, 8]))
print(solution([11, 12, 5, 5, 3, 11, 7, 12, 15, 12, 12, 11, 12, 12, 7, 8, 12, 11, 12, 7, 12, 5, 15, 20, 15, 12, 15, 12, 15, 14, 12]))
