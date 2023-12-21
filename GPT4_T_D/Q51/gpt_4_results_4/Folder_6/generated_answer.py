
def if_contains_anagrams(lst):
    from itertools import combinations
    from collections import Counter

    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())

    word_combs = combinations(lst, 2)
    anagram_count = 0

    for word1, word2 in word_combs:
        if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
            anagram_count += 1
        if anagram_count > 86:
            return False
    return True
