
from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if Counter(strings[i].lower()) == Counter(strings[j].lower()) and len(strings[i]) >= 3 and len(strings[j]) >= 3:
                anagram_count += 1

    if anagram_count <= 15:
        return True
    else:
        return False
