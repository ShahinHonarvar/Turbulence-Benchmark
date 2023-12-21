
from collections import Counter

def if_contains_anagrams(strings):
    count = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                str1 = strings[i].lower()
                str2 = strings[j].lower()
                if Counter(str1) == Counter(str2):
                    count += 1
                    if count >= 97:
                        return True

    return False
