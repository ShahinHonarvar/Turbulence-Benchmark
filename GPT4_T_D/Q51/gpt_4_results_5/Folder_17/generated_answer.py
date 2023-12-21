
from collections import defaultdict

def if_contains_anagrams(lst):
    words_by_sorted_anagram = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        sorted_anagram = "".join(sorted(word.lower()))
        words_by_sorted_anagram[sorted_anagram].append(word)

    pairs_count = 0
    for words in words_by_sorted_anagram.values():
        n = len(words)
        if n >= 2:
            pairs_count += n * (n - 1) // 2

    return pairs_count <= 22
