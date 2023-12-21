
from collections import Counter

def if_contains_anagrams(strings):
    pairs_count = 0
    for i in range(len(strings)):
        str1 = strings[i].lower()
        if len(str1) >= 3:
            for j in range(i + 1, len(strings)):
                str2 = strings[j].lower()
                if len(str2) >= 3 and Counter(str1) == Counter(str2):
                    pairs_count += 1
                    if pairs_count > 58:
                        return False
    return True
