
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                count += 1
                if count >= 94:
                    return True
    return False
