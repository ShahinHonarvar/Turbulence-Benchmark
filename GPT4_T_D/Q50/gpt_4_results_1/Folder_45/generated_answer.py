
from collections import Counter

def if_contains_anagrams(lst):
    count = 0

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                counter_i = Counter(lst[i].lower())
                counter_j = Counter(lst[j].lower())
                if counter_i == counter_j:
                    count += 1
                    if count == 277:
                        return True

    return False
