
from collections import Counter

def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        count_i = Counter(strings[i].lower())
        for j in range(i + 1, len(strings)):
            count_j = Counter(strings[j].lower())
            if count_i == count_j:
                pairs += 1
                if pairs > 3:
                    return False
    return True
