from collections import Counter
def solution(str):
    cnt = Counter(str)
    odd_cnt = 0
    for key in cnt:
        if cnt[key] %2 == 1:
            if odd_cnt>=1:
                return False
            else: odd_cnt+=1
    return True
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))
