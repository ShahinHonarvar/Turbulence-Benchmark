
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        if len(strings[i]) >= 3:
            for j in range(i + 1, len(strings)):
                if len(strings[j]) >= 3:
                    if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                        count += 1
                        if count > 60:
                            return False
    return True
