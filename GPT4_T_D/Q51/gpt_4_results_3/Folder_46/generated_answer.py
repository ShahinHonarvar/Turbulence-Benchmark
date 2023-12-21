
from collections import defaultdict

def if_contains_anagrams(word_list):
    anagrams = defaultdict(list)
    for word in word_list:
        anagrams[''.join(sorted(word.lower()))].append(word)

    anagram_pairs = 0
    for key, values in anagrams.items():
        if len(values) >= 2 and len(key) >= 3:
            anagram_pairs += len(values) * (len(values) - 1) // 2

    if anagram_pairs <= 61:
        return True
    else:
        return False
