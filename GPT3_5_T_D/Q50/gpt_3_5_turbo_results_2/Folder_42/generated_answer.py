
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i, word in enumerate(lst):
        for j in range(i+1, len(lst)):
            if len(word) >= 3 and len(lst[j]) >= 3:
                if Counter(word.lower()) == Counter(lst[j].lower()):
                    count += 1
                    if count >= 233:
                        return True
    return False
