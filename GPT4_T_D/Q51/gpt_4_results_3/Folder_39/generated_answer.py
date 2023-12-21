
from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    for i in range(len(lst)):
        lst[i] = ''.join(sorted(lst[i].lower()))
        
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if Counter(lst[i]) == Counter(lst[j]):
                    cnt += 1
            if cnt > 257:
                return False
    return True
