
from collections import defaultdict

def if_contains_anagrams(lst):
    words = defaultdict(set)
    anagram_count = 0

    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in words and word not in words[sorted_word]:
                anagram_count += len(words[sorted_word])
            words[sorted_word].add(word)

    return anagram_count <= 65
