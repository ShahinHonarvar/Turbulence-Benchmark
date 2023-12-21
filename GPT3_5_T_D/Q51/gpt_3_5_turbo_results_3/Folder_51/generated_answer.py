
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)-1):
        string1 = strings[i].lower()
        if len(string1) < 3:
            continue
        for j in range(i+1, len(strings)):
            string2 = strings[j].lower()
            if len(string2) < 3:
                continue
            if Counter(string1) == Counter(string2):
                count += 1
                if count > 116:
                    return False
    return True
