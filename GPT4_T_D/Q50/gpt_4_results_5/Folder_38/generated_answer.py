
from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > 2 and Counter(lst[i].lower()) == Counter(lst[j].lower()):
                cnt += 1
                if cnt == 24:
                    return True
    return False
