
from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            s1,s2 = lst[i].lower(), lst[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if Counter(s1) == Counter(s2):
                    cnt += 1
    if cnt <= 11:
        return True
    else:
        return False
