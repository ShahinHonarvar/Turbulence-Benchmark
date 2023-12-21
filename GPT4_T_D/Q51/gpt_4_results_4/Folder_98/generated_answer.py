
from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j])>=3:
                str1 = "".join(sorted(lst[i].lower()))
                str2 = "".join(sorted(lst[j].lower()))
                if Counter(str1) == Counter(str2):
                    pairs += 1
                    if pairs > 46:
                        return False
    return True
