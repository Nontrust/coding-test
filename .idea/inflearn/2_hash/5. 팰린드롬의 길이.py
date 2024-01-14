from collections import Counter
def solution(s):
    answer = len(s)
    has_odd_val = False
    cnt = Counter(s)
    for key in cnt:
        if cnt[key]%2 == 1 :
            if not has_odd_val:
                has_odd_val = True
            else: answer-= 1
    return answer
    
                   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
