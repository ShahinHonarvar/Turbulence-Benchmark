
from collections import defaultdict

def if_contains_anagrams(words):
    letter_dict = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            letter_dict[''.join(sorted(word.lower()))].append(word)
    anagram_pairs = sum(len(val) * (len(val) - 1) // 2 for val in letter_dict.values())
    return anagram_pairs >= 91
