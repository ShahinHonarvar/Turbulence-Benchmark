
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if_strings = strings[i].lower()
            compared_strings = strings[j].lower()
            if len(if_strings) == len(compared_strings) and Counter(if_strings) == Counter(compared_strings):
                count += 1
                if count > 26:
                    return False
    return True
