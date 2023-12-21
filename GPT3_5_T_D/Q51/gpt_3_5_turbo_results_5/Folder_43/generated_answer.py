
from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        count_i = Counter(strings[i].lower())
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[i]) == len(strings[j]):
                if count_i == Counter(strings[j].lower()):
                    anagram_count += 1
                    if anagram_count > 3:
                        return False
    return True
