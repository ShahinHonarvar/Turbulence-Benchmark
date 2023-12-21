
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    anagram_counts = defaultdict(int)
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        for other_word in lst:
            other_word = other_word.lower()
            if word != other_word and is_anagram(word, other_word):
                pair = frozenset([word, other_word])
                anagram_counts[pair] += 1

    return len(anagram_counts) <= 6
