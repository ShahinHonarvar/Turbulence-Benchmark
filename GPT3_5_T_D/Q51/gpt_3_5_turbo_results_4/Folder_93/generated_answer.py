
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and lst[i].lower() != lst[j].lower():
                if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    count += 1
                    if count > 36:
                        return False
    return True
