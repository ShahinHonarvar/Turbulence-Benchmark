
from collections import defaultdict

def if_contains_anagrams(lst):
    words_count = defaultdict(int)
    anagrams_count = 0

    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            anagrams_count += words_count[sorted_word]
            words_count[sorted_word] += 1

    return anagrams_count <= 69
