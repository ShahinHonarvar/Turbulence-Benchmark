
import itertools

def if_contains_anagrams(lst):
    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())

    count = 0
    for word1, word2 in itertools.combinations(lst, 2):
        if len(word1) >= 3 and len(word2) >= 3 and is_anagram(word1, word2):
            count += 1
            if count > 24:
                return False

    return True
