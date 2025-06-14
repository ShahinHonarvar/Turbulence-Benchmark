
from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs_count = 0

    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                    anagram_pairs_count += 1

                    if anagram_pairs_count >= 136:
                        return True

    return False
