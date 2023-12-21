
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if Counter(lst[i].lower()) == Counter(lst[j].lower()) and len(lst[i]) >= 3 and len(lst[j]) >= 3:
                count += 1
                if count > 116:
                    return False
    return True
