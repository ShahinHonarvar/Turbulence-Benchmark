
from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and strings[i].lower() == strings[j].lower():
                count += 1
    if count >= 123:
        return True
    else:
        return False
