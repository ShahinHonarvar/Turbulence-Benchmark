
from collections import Counter

def if_contains_anagrams(lst):
    def count_anagrams(lst):
        pairs = 0
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if len(lst[i]) >= 3 and len(lst[j]) >= 3 and Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    pairs += 1
        return pairs

    if count_anagrams(lst) > 59:
        return False
    else:
        return True
